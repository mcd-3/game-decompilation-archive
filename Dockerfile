FROM ubuntu:25.04

# Install dependencies needed for all the decompilation projects
RUN apt-get update && apt-get install -y --no-install-recommends \
    binutils-mips-linux-gnu \
    bsdmainutils \
    build-essential \
    ca-certificates \
    cmake \
    cpp-mips-linux-gnu \
    curl \
    gcc-mips-linux-gnu \
    git \
    libaudiofile-dev \
    libbz2-dev \
    libc6-dev-i386 \
    libcapstone-dev \
    libpng-dev \
    libxml2-dev \
    linux-headers-generic \
    linux-libc-dev \
    make \
    pip \
    pkg-config \
    pkgconf \
    python3 \
    python3-pip \
    python3-venv \
    wget \
    xxd \
    zlib1g-dev\
    vim

# Install Rust and Pigment64 for Paper Mario Decompilation 
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Setup armips (dependency for Perfect Dark Decompilation)
RUN git clone --recursive https://github.com/Kingcom/armips.git
RUN cd armips && mkdir build && cd build
RUN cd armips && cmake -DCMAKE_BUILD_TYPE=Release .
RUN cd armips && cmake --build .
RUN cd armips && cp ./armips /bin

# Set up roms and project directories
RUN mkdir roms
RUN mkdir projects
RUN mkdir projects/n64
RUN mkdir projects/gc
WORKDIR /projects/n64

# Clone all decompilation projects
RUN git clone https://github.com/n64decomp/sm64.git
RUN git clone https://github.com/zeldaret/oot.git
RUN git clone https://github.com/zeldaret/mm.git
RUN git clone https://github.com/pmret/papermario.git
RUN git clone https://github.com/n64decomp/perfect_dark.git
RUN git clone https://gitlab.com/banjo.decomp/banjo-kazooie.git
RUN git clone https://github.com/n64decomp/mk64.git --recurse-submodules
RUN git clone https://github.com/Gillou68310/DukeNukemZeroHour.git --recursive
RUN git clone --recursive https://github.com/harvestwhisperer/hm64-decomp.git
## NOTE: This project requires the official N64 SDK and Windows XP. We can't build this in our image
##       Regardless, it's included for archival purposes
RUN git clone https://github.com/Erick194/DOOM64-RE.git

WORKDIR /projects

# Setup project level dependencies (if they have)
## Paper Mario
RUN python3 -m pip config set global.break-system-packages true
RUN cd n64/papermario \
    && ./install_deps.sh --break-system-packages \
    && ./install_compilers.sh --break-system-packages \
    && cargo install pigment64 crunch64-cli

## Banjo-Kazooie
RUN cd n64/banjo-kazooie \
    && apt-get install -y $(cat packages.txt) \
    && git submodule update --init --recursive \
    && python3 -m venv .venv \
    && .venv/bin/python3 -m pip install -r requirements.txt
### Unsure why, but the BK decomp seems to be missing some dependencies
### Let's copy it from perfect_dark for now
RUN cp /projects/n64/perfect_dark/src/include/sgidefs.h /projects/n64/banjo-kazooie/include/sgidefs.h
RUN cp -r /projects/n64/perfect_dark/include/sys /projects/n64/banjo-kazooie/include/

## Duke Nukem Zero Hour
RUN cd n64/DukeNukemZeroHour \
    && pip3 install -U splat64[mips] \
    && pip3 install -r requirements.txt

## Harvest Moon 64
RUN cd n64/hm64-decomp \
    && chmod +x tools/setup.sh \
    && tools/setup.sh

COPY ./roms /roms
COPY ./scripts /scripts
COPY ./games.json /scripts/_games.json
RUN echo 'alias gda-pull="python3 /scripts/pull.py"' >> ~/.bashrc
RUN echo 'alias gda-list="python3 /scripts/list.py"' >> ~/.bashrc
RUN echo 'alias gda-setup="python3 /scripts/setup.py"' >> ~/.bashrc
import os

def print_header(game_name):
    print(f"Setting up {game_name}")
    print("======================")

def sm64(version):
    print_header("Super Mario 64")

    print("""
    ### The SM64 decompilation is no longer actively maintained
    ### There is a bug within the bbh linker map fixed here:
    ###
    ### https://github.com/n64decomp/sm64/pull/99
    ###
    ### If you encounter an error like this:
    ###    " mips64-elf-ld: build/us/levels/bbh/leveldata.o:(.data+0x6dfc): undefined reference to spooky_09004800 "
    ### you'll need to apply the fix located in the above Pull Request to the Makefile
    """)

    os.system(f"cp /roms/sm64/{version}.z64 /projects/n64/sm64/baserom.{version}.z64")
    os.system(f"cd /projects/n64/sm64 && make VERSION={version}")

def paper_mario(version):
    project_location = "/projects/n64/papermario"
    cd_cmd = f"cd {project_location} &&"

    print_header("Paper Mario")
    os.system(f"cp /roms/papermario/{version}.z64 {project_location}/ver/{version}/baserom.z64")
    os.system(f"{cd_cmd} ./install_deps.sh")
    os.system(f"{cd_cmd} ./install_compilers.sh")
    os.system(f"{cd_cmd} && ./configure")
    os.system(f"{cd_cmd} && ninja")

def ocarina_of_time(version):
    print_header("Ocarina of Time")
    os.system(f"cp /roms/oot/{version}.z64 /projects/n64/oot/baseroms/{version}/baserom.z64")
    os.system(f"cd /projects/n64/oot && make setup && make")


def majoras_mask(version):
    print_header("Majora's Mask")
    os.system(f"cp /roms/mm/{version}.z64 /projects/n64/mm/baseroms/n64-{version}/baserom.z64")
    os.system(f"cd /projects/n64/mm && make init -j 2")

def banjo_kazooie(version):
    print_header("Banjo-Kazooie")

    baserom = version
    if version == "us10":
        baserom = "us.v10"
    elif version == "us11":
        baserom = "us.v11"

    os.system(f"cp /roms/banjo-kazooie/{version}.z64 /projects/n64/banjo-kazooie/baserom.{baserom}.z64")
    os.system(f"cd /projects/n64/banjo-kazooie && make")

def harvest_moon(version):
    print_header("Harvest Moon 64")
    os.system(f"cp /roms/hm64-decomp/{version}.z64 /projects/n64/hm64-decomp/baserom.{version}.z64")
    os.system(f"cd /projects/n64/hm64-decomp && make setup && make")

def perfect_dark(version):
    project_location = "/projects/n64/perfect_dark"
    cd_cmd = f"cd {project_location} &&"

    print_header("Perfect Dark")
    os.system(f"cp /roms/perfect_dark/{version}.z64 {project_location}/pd.{version}.z64")
    os.system(f"{cd_cmd} git submodule update --init --recursive")
    os.system(f"{cd_cmd} make extract")
    os.system(f"{cd_cmd} make -j")

def duke_nukem(version):
    print_header("Duke Nukem Zero Hour")
    os.system(f"cp /roms/DukeNukemZeroHour/{version}.z64 /projects/n64/DukeNukemZeroHour/baserom.{version}.z64")
    os.system(f"cd /projects/n64/DukeNukemZeroHour && make setup && make --jobs")

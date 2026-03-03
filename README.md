# Game Decompilation Archiver

Docker image to set up a game decompilation project environment to build and develop various retro game decompilations.

## Set up
Before setting up, make sure you have your legally obtained ROM files for each decompilation project (including all the versions you want to set up with). We cannot give you instructions on how to legally obtain ROM files, nor can we provide you with any.

Once you have all the files you need, do the following:
1. Take your ROM file and place it in the respective game directory in the `/roms` directory
2. Rename the rom to the version name + `.z64`
3. Do steps 1 and 2 for every game and version you want to have within the archive
- Ex: If you have the US version of a Super Mario 64 ROM, copy it to `roms/sm64/` as `us.z64`. It should look like `roms/sm64/us.z64`

## Supported Projects
### Nintendo 64
|Game                 |Project URL                                       |Versions                       |
|---------------------|--------------------------------------------------|-------------------------------|
|Super Mario 64       | https://github.com/n64decomp/sm64                | `us`, `pal`, `jp`, `cn`, `sh` |
|Ocarina of Time      | https://github.com/zeldaret/oot                  | `ntsc-1.0`, `ntsc-1.1`, `pal-1.0`, `ntsc-1.2`, `pal-1.1`, `gc-jp`, `gc-jp-mq`, `gc-us`, `gc-us-mq`, `gc-eu-mq-dbg`, `gc-eu`, `gc-eu-mq`, `gc-jp-ce`, `ique-cn` |
|Majora's Mask        | https://github.com/zeldaret/mm                   | `us`                          |
|Banjo Kazooie        | https://gitlab.com/banjo.decomp/banjo-kazooie    | `us10`, `us11`, `pal`, `jp`   |
|Paper Mario          | https://github.com/pmret/papermario              | `us`, `jp`, `pal`, `ique`     |
|Perfect Dark         | https://github.com/n64decomp/perfect_dark        | `ntsc-final`, `ntsc-beta`, `ntsc-1.0`, `pal-beta`, `pal-final`, `jpn-final` |
|Duke Nukem: Zero Hour| https://github.com/Gillou68310/DukeNukemZeroHour | `us`                          | 
|Harvest Moon 64      | https://github.com/harvestwhisperer/hm64-decomp  | `us`, `jp`                    |

#### Building Issues (Unsupported)
|Game          |Project URL                            |Versions              |
|--------------|---------------------------------------|----------------------|
|Mario Kart 64 | https://github.com/n64decomp/mk64     | `us`, `eu10`, `eu11` | 

#### Windows Only (Unsupported)
|Game    |Project URL                            |Versions |
|--------|---------------------------------------|---------|
|Doom 64 | https://github.com/Erick194/DOOM64-RE | `us`    | 
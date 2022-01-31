# gps_alire
Plugin for GNAT studio to load environment variables of alire projects

Alire is a package manager for Ada projects that adapts `.gpr` files to link external crates.
GPS per default cannot handle this as of the 2021 community edition.

This repo provides a GPS plugin to automatically set needed environment variables for Ada projects
that use the Alire package manager.

# Usage

**Note:** A working Alire setup is assumed and no GNAT studio is open.

1. Copy `alire.py` into `.gnatstudio/plug-ins`

   `.gnatstudio` should be located in your user directory.

2. Open your `.gpr` project
3. The GNAT studio message output shows that an Alire project was found

# Credit

The original idea is from https://github.com/valexey/gnatstudio_alire_integration/blob/master/alire.py.
It was adapted to work with Alire 1.1.x.

# License

MIT Licensed

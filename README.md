# Thermod Button-LED monitor
Thermod monitor for Raspberry Pi with one button and one RGB LED.

The LED reports the current status of the thermostat, while the button can be
used to change the status in a, almost, sequential way: from any status to
`auto` and from `auto` to `tmax` on first pressing, then from `tmax` to
`off`, from `off` to `tmin`, from `tmin` to `antifreeze` and from
`antifreeze` to `auto`.

## License
Thermod DB-Stats monitor v1.1.0 \
Copyright (C) 2018 Simone Rossetto <simros85@gmail.com> \
GNU General Public License v3

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


## How to install

### Requirements
*Thermod Button-LED monitor* requires [Python3](https://www.python.org/)
(at least version 3.5) and the packages:

 - [thermod](https://github.com/droscy/thermod) (>=1.0.0)
 - [requests](http://docs.python-requests.org/) (>=2.4.3)
 - [gpiozero](https://github.com/RPi-Distro/python-gpiozero) (>= 1.3.0)

**Note:** this monitor is already included in [Thermod v1.0.0](https://github.com/droscy/thermod/tree/1.0.0),
then it has been removed and put in a separate repository since commit
[82a92f8](https://github.com/droscy/thermod/commit/82a92f8387802357a32f800c33da3efe434c7f3b).

### Installation
To install the *Button-LED monitor* first uncompress the tarball and run

```bash
python3 setup.py install
```

### Building and installing on Debian-based system
A Debian package can be build using
[git-buildpackage](https://honk.sigxcpu.org/piki/projects/git-buildpackage/).

Assuming you have already configured your system to use git-buildpackage
(if not see Debian Wiki for [git-pbuilder](https://wiki.debian.org/git-pbuilder),
[cowbuilder](https://wiki.debian.org/cowbuilder),
[Packaging with Git](https://wiki.debian.org/PackagingWithGit) and
[Using Git for Debian Packaging](https://www.eyrie.org/~eagle/notes/debian/git.html))
then these are the basic steps:

```bash
git clone https://github.com/droscy/thermod-monitor-buttonled.git
cd thermod-monitor-buttonled
git branch --track pristine-tar origin/pristine-tar
git checkout -b debian/master origin/debian/master
gbp buildpackage
```

The package can then be installed as usual:

```bash
dpkg -i thermod-monitor-buttonled_{version}_{arch}.deb
```


## Starting/Stopping the monitor
To start *Button-LED monitor* from the same system where Thermod is
running simply execute

```bash
thermod-monitor-buttonled
```

If Thermod is running on a *different* system, the option `--host` can be set
to the hostname of that system.

The PIN on Raspberry Pi for each color of RGB LED and for the Button can be
changed using command line parameters: `--red`, `--green`, `--blue`
and `--button`. The default values are:

 - *red* 17
 - *green* 27
 - *blue* 22
 - *button* 5

To have the full list of available options run `thermod-monitor-buttonled`
with `--help` option.

### Systemd
If *systemd* is in use, copy the file `thermod-monitor-buttonled.service`
to folder `/lib/systemd/system`, change it to meet your requirements
then execute

```bash
systemctl daemon-reload
systemctl enable thermod-monitor-buttonled.service
```

to automatically start the monitor at system startup.

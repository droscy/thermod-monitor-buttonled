# Thermod Button-LED monitor
Thermod monitor for Raspberry Pi with one button and one RGB LED.

The LED reports the current status of the thermostat, while the button can be
used to change the status in a sequential way: from any status to
`auto` and from `auto` to `tmax` on first pressing, then from `tmax` to
`tmin`, from `tmin` to `antifreeze`, and so on.

## License
Thermod Button-LED monitor v1.2.0-beta1 \
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
(at least version 3.5) and the following packages:

 - [thermod](https://github.com/droscy/thermod) (>=1.0.0, <2.0.0)
 - [requests](http://docs.python-requests.org/) (>=2.4.3)
 - [gpiozero](https://github.com/RPi-Distro/python-gpiozero) (>= 1.3.0)

**Note:** this monitor is already included in [Thermod v1.0.0](https://github.com/droscy/thermod/tree/1.0.0),
then it has been removed and put in a separate repository since commit
[82a92f8](https://github.com/droscy/thermod/commit/82a92f8387802357a32f800c33da3efe434c7f3b).

### Installation
To install *Button-LED monitor* you need to have [Python3](https://www.python.org/)
and [virtualenv](https://virtualenv.pypa.io/en/stable/) already installed on
the system, then the basic steps are:

 1. download and uncompress the source tarball (or clone the repository)

 2. create e virtualenv somewhere

 3. install [thermod](https://github.com/droscy/thermod) package in that virtualenv (see its readme on how to install)

 4. using the same virtualenv, install *Button-LED monitor* with

       ```bash
       python3 setup.py install
       ```

 5. copy the config file `monitor-buttonled.conf` in one of the following folder (the top-most take precedence)

    - `~/.thermod/`
    - `~/.config/thermod/`
    - `/usr/local/etc/thermod/`
    - `/var/lib/thermod/`
    - `/etc/thermod/`

    and adjust it to your needs.

### Building and installing on Debian-based system
A Debian package can be build using
[git-buildpackage](https://honk.sigxcpu.org/piki/projects/git-buildpackage/).

Assuming you have already configured your system to use git-buildpackage
(if not see Debian Wiki for [git-pbuilder](https://wiki.debian.org/git-pbuilder),
[cowbuilder](https://wiki.debian.org/cowbuilder),
[Packaging with Git](https://wiki.debian.org/PackagingWithGit) and
[Using Git for Debian Packaging](https://www.eyrie.org/~eagle/notes/debian/git.html))
and cloned the repository, then do:

```bash
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
After having edited the config file `monitor-buttonled.conf` you can
start *Button-LED monitor* simply executing

```bash
thermod-monitor-buttonled
```

To have the full list of available options run the monitor with `--help` option.

### Systemd
If *systemd* is in use, copy the file `thermod-monitor-buttonled.service`
to `/lib/systemd/system` or to `/usr/local/lib/systemd/system`, change it
to your needs then execute the following commands to automatically start
the monitor at system startup.

```bash
systemctl daemon-reload
systemctl enable thermod-monitor-buttonled.service
```


## LED flickering issue
If you use a *very* low value for brightness (like 0.2-0.3) and your LED
suffers from flickering, probably the PWM of your board is controlled via software.

To avoid the flickering you can try to use [pigpio](http://abyz.me.uk/rpi/pigpio/)
as backend driver for `gpiozero`:

 1. make sure to have the `pigpiod` daemon running on the system

 2. install the `pigpio` package in the same virtualenv of `thermod-monitor-buttonled`

       ```bash
       pip install pigpio
       ```

 3. start *Button-LED monitor* with the environment variable `GPIOZERO_PIN_FACTORY`
    set to `pigpio`:

       ```bash
       GPIOZERO_PIN_FACTORY=pigpio thermod-monitor-buttonled
       ```

    or, if you are using *systemd*, you can add to `thermod-monitor-buttonled.service`

       ```
       Environment=GPIOZERO_PIN_FACTORY=pigpio
       ```

For more information on `pigpio` daemon and backend driver see its [web page](http://abyz.me.uk/rpi/pigpio/)
and `gpiozero` [documentation](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html#environment-variables).


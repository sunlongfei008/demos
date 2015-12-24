ICE中间件DEMO
============================================================

python开发,ICE中间件

#目录简介
        services:服务端源码
        test:测试程序

#运行
##先运行services中的服务端
$ python service.py

##在新的窗口中运行test中的客户端
$ python client.py

#依赖包安装

##Ice源码下载地址

https://codeload.github.com/zeroc-ice/ice/tar.gz/v3.6.1

##操作系统平台相关依赖包安装

        Platform        Instructions

        Windows         Download the Web Installer(exe) or the Offline Installer(msi)
                        http://zeroc.com/download/Ice/3.6/Ice-3.6.1-WebInstaller.exe
                        http://zeroc.com/download/Ice/3.6/Ice-3.6.1.msi.

        OS X            Using [Homebrew](http://brew.sh/):

                            brew install ice

                        The IceGrid Admin app is not installed by default with Homebrew.
                        Download IceGridAdmin-3.6.1.dmg to install it.
                        http://zeroc.com/download/Ice/3.6/IceGridAdmin-3.6.1.dmg

        Ubuntu          Ubuntu 15.10 using apt-get:

                            wget https://zeroc.com/download/GPG-KEY-zeroc-release
                            sudo apt-key add GPG-KEY-zeroc-release
                            sudo apt-add-repository \
                              "deb http://zeroc.com/download/apt/ubuntu15.10 stable main"
                            sudo apt-get update
                            sudo apt-get install zeroc-ice-all-runtime zeroc-ice-all-dev

                        Ubuntu 15.04 using apt-get:

                            wget https://zeroc.com/download/GPG-KEY-zeroc-release
                            sudo apt-key add GPG-KEY-zeroc-release
                            sudo apt-add-repository \
                              "deb http://zeroc.com/download/apt/ubuntu15.04 stable main"
                            sudo apt-get update
                            sudo apt-get install zeroc-ice-all-runtime zeroc-ice-all-dev

                        Ubuntu 14.04 using apt-get:

                            wget https://zeroc.com/download/GPG-KEY-zeroc-release
                            sudo apt-key add GPG-KEY-zeroc-release
                            sudo apt-add-repository \
                              "deb http://zeroc.com/download/apt/ubuntu14.04 stable main"
                            sudo apt-get update
                            sudo apt-get install zeroc-ice-all-runtime zeroc-ice-all-dev

        Red Hat         
        Enterprise      RHEL 7 using yum:
        Linux
                            wget https://zeroc.com/download/GPG-KEY-zeroc-release
                            sudo rpm --import GPG-KEY-zeroc-release
                            cd /etc/yum.repos.d
                            sudo wget https://zeroc.com/download/rpm/zeroc-ice-el7.repo
                            sudo yum install ice-all-runtime ice-all-devel

                        RHEL 6 using yum:

                            wget https://zeroc.com/download/GPG-KEY-zeroc-release
                            sudo rpm --import GPG-KEY-zeroc-release
                            cd /etc/yum.repos.d
                            sudo wget https://zeroc.com/download/rpm/zeroc-ice-el6.repo
                            sudo yum install ice-all-runtime ice-all-devel

        SuSE Linux 
        Enterprise      SLES 12 using zypper:
        Server    
                            wget https://zeroc.com/download/GPG-KEY-zeroc-release
                            sudo rpm --import GPG-KEY-zeroc-release
                            wget https://zeroc.com/download/rpm/zeroc-ice-sles12.repo
                            sudo zypper addrepo zeroc-ice-sles12.repo
                            sudo zypper install ice-all-runtime ice-all-devel

        SLES 11         using zypper:

                            wget https://zeroc.com/download/GPG-KEY-zeroc-release
                            sudo rpm --import GPG-KEY-zeroc-release
                            wget https://zeroc.com/download/rpm/zeroc-ice-sles11.3.repo
                            sudo zypper addrepo zeroc-ice-sles11.3.repo
                            sudo zypper install ice-all-runtime ice-all-devel

        Amazon Linux    Using yum:

                            wget https://zeroc.com/download/GPG-KEY-zeroc-release
                            sudo rpm --import GPG-KEY-zeroc-release
                            cd /etc/yum.repos.d
                            sudo wget https://zeroc.com/download/rpm/zeroc-ice-amzn1.repo
                            sudo yum install ice-all-runtime ice-all-devel


##开发语言平台相关依赖包安装

        Language            Instructions

        JavaScript          Using bower:

                                bower install ice --save

                            Using npm:

                                npm install ice --save
                                npm install slice2js --save-dev

                            Using cdnjs: https://cdnjs.com/libraries/ice

        Python              Using pip:

                                pip install zeroc-ice

        Ruby                Linux and OS X using gem:

                                gem install zeroc-ice

                            Windows 64-bit using gem:

                                gem install zeroc-ice-x64-mingw

                            Windows 32-bit using gem:

                                gem install zeroc-ice-x86-mingw

        Php                 Linux and OS X

                                wget https://github.com/zeroc-ice/ice/archive/v3.6.1.tar.gz
                                tar zvxf v3.6.1.tar.gz
                                cd ice-3.6.1/php/
                                export ICE_HOME=/usr
                                make
                                make install
                                /bin/cp /opt/Ice-3.6.1/php/IcePHP.so /usr/local/php-5.5.18/lib/php/extensions/no-debug-non-zts-20121212/


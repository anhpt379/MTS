#! /usr/bin/env python
#! coding: utf-8
# pylint: disable-msg=W0311
data = """
Downloads

Stable release

The 1.2 branch features substantial improvements. [List to be written still, sorry!]

The latest stable release is 1.2.0:

xapian-core: the Xapian library itself [news]
omega: Omega - an application built on Xapian, consisting of indexers and a CGI search frontend. [news]
xapian-bindings: SWIG and JNI bindings allowing Xapian to be used from various other programming languages [news]
Search::Xapian: Perl bindings (on CPAN) [news] (on CPAN)
The wiki contains a summary of bugs, patches, and workarounds relating to the latest release.

The latest 1.0 release is 1.0.20:

xapian-core: the Xapian library itself [news]
omega: Omega - an application built on Xapian, consisting of indexers and a CGI search frontend. [news]
xapian-bindings: SWIG and JNI bindings allowing Xapian to be used from various other programming languages [news]
Search::Xapian: Perl bindings (on CPAN) [news] (on CPAN)
Debian and Ubuntu packages

Packages of xapian-core, xapian-omega, and xapian-bindings (Python, PHP, Ruby, and Tcl) are available from the Debian and Ubuntu archives for all currently supported releases except Ubuntu 6.06 (dapper). The Perl bindings are also available from the archives for everything except Debian etch and Ubuntu dapper (the package name is libsearch-xapian-perl).

Backported Debian packages of newer versions are available from backports.org.

Backported Ubuntu packages of newer versions are available from a Personal Package Archive (PPA) on Launchpad maintained by Olly Betts. Follow the instructions on that link for how to make use of these. Currently all packages are backported to all Ubuntu releases which are still supported, except that the Perl bindings aren't backported to Ubuntu 6.06 (dapper) (because the packaging relies heavily on newer features of debhelper).

RPM packages

Fedora

Fedora 7 and newer have RPM packages for Xapian in their default repositories, though these may lag behind the latest releases a bit.

RedHat Enterprise Linux

Tim Brody has built RPM packages for RedHat Enterprise Linux 4 and RedHat Enterprise Linux 5 - there are binary packages for i386 and source RPMs.

If you have RHEL 5, copy xapian.repo into /etc/yum.repos.d/ and then you can install the packages using yum:

$ su
enter your root password
# cd /etc/yum.repos.d
# rm -f xapian.repo
# wget http://www.xapian.org/RPM/rhel5/xapian.repo
# yum install xapian-omega xapian-bindings-php xapian-bindings-python xapian-bindings-tcl8
For RHEL 4, use this xapian.repo instead if you are using DAG's yum. Otherwise you can download the individual packages and install them by hand.

Source RPMs

The source RPMs (the three files that end in ".src.rpm") are not distribution specific - you can build binary RPMs from those if binary packages aren't available for your architecture or distribution like so:

$ rpmbuild --rebuild PACKAGENAME.src.rpm
Other RPM-based distributions

These RPM-based distributions have their own RPM packages which might be better tailored:

ALT Linux RPMs of xapian-core only
SuSE RPMs of xapian-core and omega (and instructions for use)
Other Linux Distributions

Gentoo Portage has ebuilds for xapian-core and xapian-bindings
FrugalWare Linux has packaged xapian-core.
Zenwalk Linux has packaged xapian-core.
archlinux has packaged xapian-core, xapian-bindings (Python and PHP), and Perl Search::Xapian.
FreeBSD Ports Collection

The FreeBSD Ports Collection has packages for xapian-core, xapian-omega, xapian-bindings (Python and PHP), and Search::Xapian.

NetBSD pkgsrc

The NetBSD pkgsrc collection has packages for xapian-core, xapian-omega, and Search::Xapian.

OpenBSD

OpenBSD Ports has packages for xapian-core and xapian-omega.

Mac OS X

The Fink project has packages for xapian-core, Omega, and the Python and Ruby bindings.

Alternatively, MacPorts has packages for xapian-core.

Cygwin

Packages for xapian-core, xapian-bindings, and Search::Xapian are available from Cygwin Ports. Packages for Omega aren't there yet, but 
"""
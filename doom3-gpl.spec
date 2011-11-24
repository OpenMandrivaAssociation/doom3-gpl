%define	gitrevision	15597777fc31d6d9fe0d48848e5c97b07e470b79

Summary:	Complete independent Doom3 game
Name:		doom3-gpl
Version:	1.0
#if you want to update it
#just change rel version and git revision
Release:	1
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv3
Group:		Games/Other
Url:		https://github.com/TTimo/doom3.gpl.git
BuildRequires:	scons
BuildRequires:	openal-devel
BuildRequires:	curl-devel
BuildRequires:	jpeg-devel
BuildRequires:	GL-devel
BuildRequires:	libalsa-devel
BuildRequires:	libxext-devel

%description
Doom3 under GPLv3
Doom 3 is a science fiction horror video game developed by id Software and published by Activision.
An example of the first-person shooter genre.
You must place *.pak files from yoor Doom3 CD-disc into /usr/games/doom3/

%prep
%setup -q

%build

sed -i '/#define LINUX_DEFAULT_PATH.*"\/usr\/local\/games\/doom3/s/$/\n#define LINUX_DEFAULT_PATH "\/usr\/games\/doom3"/' neo/framework/Licensee.h

cd neo/
%scons

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_prefix}/games/doom3
mkdir -p %{buildroot}%{_libdir}/neo/

install -D -m 0644 neo/gamex86-d3xp.so %{buildroot}/%{_libdir}/neo/gamex86-d3xp.so
install -D -m 0644 neo/gamex86-d3xp.so %{buildroot}/%{_libdir}/neo/gamex86-base.so
install -D -m 0755 neo/doom.x86 %{buildroot}/%{_bindir}/doom.x86
touch %{buildroot}%{_prefix}/games/doom3/put_pak_files.here



%files
%{_libdir}/neo/gamex86-d3xp.so
%{_prefix}/games/doom3/put_pak_files.here
%{_libdir}/neo/gamex86-base.so
%{_bindir}/doom.x86

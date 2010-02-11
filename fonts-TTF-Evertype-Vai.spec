Summary:	Free TrueType fonts for the Vai script
Summary(pl.UTF-8):	Wolnodostępne fonty TrueType dla pisma vai
Name:		fonts-TTF-Vai_Slant_Unicode
Version:	1.0
Release:	1
License:	SIL OFL, distributable
Group:		Fonts
Source0:	http://www.evertype.com/fonts/vai/dukorfont.zip
# Source0-md5:	77de905be86c9b59ab4691ef6ad3e588
Source1:	http://www.evertype.com/fonts/vai/wakorfont.zip
# Source1-md5:	125d46d683401cb8d2fcc8c18a237264
URL:		http://www.evertype.com/fonts/vai/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
These are two Vai fonts, Dukor, which was based on glyphs drawn
originally by calligrapher Jason Glavy, and Wakor, which was based on
the SIL Vai font - the one that was used in the Vai New Testament in
2002. Both fonts have both plain and italic faces, and both have
additions needed for older Vai orthography.

%prep
%setup -q -c -a1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

# remove uploader name from the font file name
install */[DW]*.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc */*.txt
%{ttffontsdir}/Dukor*.ttf
%{ttffontsdir}/Wakor*.ttf

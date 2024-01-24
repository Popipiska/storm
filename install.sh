PC_YELLOW='\e[0;33m%s\e[m\n'

printf "    ${PC_YELLOW}" "Installing python3"
{
  apt install -y python3
} >&-

printf "    ${PC_YELLOW}" "Installing python3-pip"
{
  apt install -y python3-pip
} >&-

printf "    ${PC_YELLOW}" "Installing unzip"
{
  apt install -y unzip
} >&-

printf "    ${PC_YELLOW}" "Installing tmux"
{
  apt install -y tmux
} >&-

printf "    ${PC_YELLOW}" "Unzipping project archive"
{
  unzip /tmp/storm-force.zip &&
  rm -rf /tmp/storm-force.zip
} >&-

printf "    ${PC_YELLOW}" "Install google-chrome"
{
  wget https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_110.0.5481.77-1_amd64.deb &&
  apt install -y software-properties-gtk &&
  apt-get install -y gconf-service &&
  dpkg -i --force-depends google-chrome-stable_110.0.5481.77-1_amd64.deb ||
  apt -y --fix-broken install &&
  dpkg -i --force-depends google-chrome-stable_110.0.5481.77-1_amd64.deb &&
  apt-mark hold chromium-browser
} >&-
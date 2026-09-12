name: Build APK

on:
  push:
    branches: [ main, master ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y \
              python3-pip \
              build-essential \
              git \
              python3-dev \
              ffmpeg \
              libsdl2-dev \
              libsdl2-image-dev \
              libsdl2-mixer-dev \
              libsdl2-ttf-dev \
              libportmidi-dev \
              libswscale-dev \
              libavformat-dev \
              libavcodec-dev \
              zlib1g-dev \
              libgstreamer1.0-dev \
              gstreamer1.0-plugins-base \
              gstreamer1.0-plugins-good \
              openjdk-17-jdk \
              autoconf \
              libtool \
              pkg-config \
              unzip \
              zip
          pip install --upgrade pip
          pip install buildozer cython==0.29.33

      - name: Build with Buildozer
        run: |
          buildozer -v android debug

      - name: Upload APK
        uses: actions/upload-artifact@v3
        with:
          name: package
          path: bin/*.apk

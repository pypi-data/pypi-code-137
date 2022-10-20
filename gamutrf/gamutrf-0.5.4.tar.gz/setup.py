# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gamutrf']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2==3.1.2',
 'bjoern==3.2.2',
 'cairocffi>=1.3.0,<2.0.0',
 'falcon-cors==1.1.7',
 'falcon==3.1.0',
 'gpsd-py3==0.3.0',
 'httpx==0.23.0',
 'matplotlib==3.6.1',
 'numpy==1.23.4',
 'paho-mqtt==1.6.1',
 'pandas==1.5.1',
 'prometheus_client==0.15.0',
 'pycairo>=1.21.0,<2.0.0',
 'requests==2.28.1',
 'schedule==1.1.0',
 'scipy==1.9.3',
 'sigmf==1.0.0',
 'zstandard==0.18.0']

entry_points = \
{'console_scripts': ['gamutrf-api = gamutrf.__main__:api',
                     'gamutrf-freqxlator = gamutrf.__main__:freqxlator',
                     'gamutrf-samples2raw = gamutrf.__main__:samples2raw',
                     'gamutrf-scan = gamutrf.__main__:scan',
                     'gamutrf-scan2mp4 = gamutrf.__main__:scan2mp4',
                     'gamutrf-scan2rtlpow = gamutrf.__main__:scan2rtlpow',
                     'gamutrf-sigfinder = gamutrf.__main__:sigfinder',
                     'gamutrf-specgram = gamutrf.__main__:specgram']}

setup_kwargs = {
    'name': 'gamutrf',
    'version': '0.5.4',
    'description': 'An orchestrated SDR scanner',
    'long_description': '# gamutRF\n\nAn SDR orchestrated scanner and collector.\n\ngamutRF is a system enabling a compact network of one or more modest machines (such as Pi4s), each with their own USB SDR (such as an Ettus\nB200mini or a BladeRF XA9), to operate collectively as a configurable wideband scanner and I/Q sample recorder.\n\nA gamutRF "orchestrator" machine can scan 0.1GHz to 6GHz in 30 seconds to identify signals, and then command potentially many gamutRF "workers" to make I/Q sample recordings for later analysis.\n\ngamutRF provides tools to work with I/Q sample recordings, and to also record GPS location/compass metadata for the system itself. gamutRF typically runs on networks of Raspberry Pi4s, but can also run on x86 machines, and is based on gnuradio.\n\nSee also [instructions on how to build a gamutRF system](BUILD.md).\n\n## Scanner theory of operation\n\ngamutRF\'s scanner function is split across two Docker containers which are both run on the orchestrator. The `gamutrf` (scanner) container connects to the SDR and sweeps over a configured frequency range in 30s, retuning at 97Hz, while sampling at 8Msps (all default values which can be changed). For example, to sweep from 5GHz to 6GHz in 30s, it covers approximately 33.3MHz/s, retuning across that 33.3MHz at 97Hz.\n\nThe samples are sent to a [streaming FFT gnuradio block](https://github.com/ThomasHabets/gr-habets39) which emits 2048 FFT points which are sent over UDP to the `sigfinder` container (see below). The FFT block needs to know when the SDR has been retuned to a new frequency, so it uses a gnuradio timestamp and frequency tag provided by the gnuradio UHD driver upon retuning. This tag functionality has been added to the Soapy driver in a gnuradio fork which is part of gamutRF, so that other SDRs may be used as scanners.\n\nThe `sigfinder` container consumes these FFT points from UDP packets, does some noise processing (correcting FFT points to be in frequency order, computing mean power over 10kHz, and then a rolling mean over 1MHz) and then submits them to [scipy.signals.find_peaks](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html).\n\nIf workers have been provisioned, the orchestrator will then command the workers to make an approximately 10 second I/Q recording at approximately 20Msps of each signal. Each signal peak is assigned a 20MHz bin, which means that if a signal is repeatedly detected with some frequency variation, the assigned recording bin will be constant, and if multiple signals are detected within 20MHz they can be collected simultaneously. A worker by default records at a higher sample rate than the bin size, so that 20MHz signal margins can be recorded.\n\nAs there will almost certainly be more signals than workers available, the orchestrator will prioritize signals that it least often observed over a configurable number of scanner cycles. It is possible to configure this to `off` so that the recording choice will be random. It is also possible to configure the workers to tell the orchestrator to exclude that worker from certain frequency ranges (if for example the worker SDR cannot handle some part of the frequency spectrum scanned).\n\n## Operating gamutRF\n\nSee the [build doc](BUILD.md)\n\n### SDR/scanner/sigfinder command line options\n\nWhile there are other options, these options primarily influence gamutRF\'s scanner functionality.\n\n#### scanner\n\n| Option | Description |\n| -- | -- |\n| --freq-start and --freq-end | Start and end of frequency range to scan in Hz (also used by sigfinger) |\n| --igain | SDR input gain in dB |\n| --sweep-sec | Time to sweep frequency range in seconds |\n| --retune-hz | Rate at which to retune SDR frequency |\n| --nfft | Number of FFT points |\n\n##### sigfinder\n\n| Option | Description |\n| -- | -- |\n| --width | Minimum width of a peak to be detected in 0.01MHz increments (passed to scipy find_peaks()) |\n| --prominence | Minimum prominence of a peak to be detected (passed to scipy find_peaks()) |\n| --threshold | Minimum threshold in dB of a peak to be detected (passed to scipy find_peaks()) |\n| --bin_width | Bin width in MHz |\n| --max_raw_power | Maximum valid raw power value at each FFT point |\n| --history | Number of scanner cycles over which to prioritize recording of least often observed peaks |\n| --record_bw_msps | Number of samples per second in units of 1024^2 (generally larger than bin size to record signal margins) |\n| --record_secs | Length of time to record I/Q samples in seconds |\n| --fftlog | Log raw output of CSV to this file, which will be rotated every --rotatesecs |\n| --fftgraph | Graph the most recent FFT signal and peaks to this PNG file (will keep the last --nfftgraph versions) |\n\n### Manually initiating worker actions\n\nThe orchestrator has a web interface on port 80. You can use this to command a worker to start an I/Q sample recording or start a RSSI stream.\n\n## Working with worker I/Q recordings\n\nWorkers make recordings that are compressed with zstandard, and are typically in complex number, int16 format, and include the center frequency and sample rate that the recording was made with. gamutRF tools can generally work with such files directly, but other tools require the recordings to be converted (see below).\n\n### Generating a spectrogram of a recording\n\ngamutRF provides a tool to convert a recording or directory of recordings into a spectrogram. For example, to convert all I/Q recordings in /tmp:\n\n```docker run -ti -v /tmp:/tmp iqtlabs/gamutrf gamutrf-specgram /tmp```\n\nUse the ```--help``` option to change how the spectogram is generated (for example, to change the sample rate).\n\n### Translating recordings to "gnuradio" format\n\nMost SDR tools by convention take an uncompressed raw binary file as input, of [gnuradio type complex](https://blog.sdr.hu/grblocks/types.html). The user must explicitly specify to most SDR tools what sample rate the file was made at to correctly process it. gamutRF provides a tool that converts a gamutRF I/Q recording (which may be compressed) to an uncompressed binary file. For example:\n\n```\ndocker run -v /tmp:/tmp -ti iqtlabs/gamutrf gamutrf-samples2raw /tmp/gamutrf_recording_ettus_directional_gain70_1234_100000000Hz_20971520sps.s16.zst\n```\n\n### Reviewing a recording interactively in gqrx\n\n[gqrx](https://gqrx.dk/) is a multiplatform open source tool that allows some basic SDR operations like visualizing or audio demodulating an I/Q sample recording (see the [github releases page](https://github.com/gqrx-sdr/gqrx/releases), for a MacOS .dmg file). To use gqrx with a gamutRF recording, first translate the recording to gnuradio format (see above). Then open gqrx.\n\n* Select ```Complex Sampled (I/Q) File```\n* Set ```Input rate``` to be the same as the gamutRF sample rate (e.g. from the recording file name,\n```gamutrf_recording_ettus_directional_gain70_1234_100000000Hz_20971520sps.raw```, set ```Input rate``` to 20971520, and also edit ```rate=``` in ```Device string``` to be 20971520)\n* Set ``Bandwidth`` to 0\n* Edit ```Device string``` to set the ```file=``` to be the path to the recording.\n* Set ```Decimation``` to None.\n* Finally select ```OK``` and then ```play``` from the gqrx interface to watch the recording play.\n\n### Reducing recording sample rate\n\nYou may want to reduce the sample rate of a recording or re-center it with respect to frequency (e.g. to use another demodulator tool that doesn\'t support a high sample rate). gamutRF provides the ```freqxlator``` tool to do this.\n\n* Translate your gamutRF recording to gnuradio format (see above).\n* Use ```freqxlator``` to create a new recording at a lower sample rate, potentially with a different center frequency.\n\nFor example, to reduce a recording made with gamutRF\'s default sample rate to 1/10th the rate while adjusting the center frequency down by 1MHz, use:\n\n```docker run -ti iqtlabs/gamutrf gamutrf-freqxlator --samp-rate 20971520 --center -1e6 --dec 10 gamutrf_recording_gain70_1234_100000000Hz_20971520sps.raw gamutrf_recording_gain70_1234_100000000Hz_2097152sps.raw```\n\n### Demodulating AM/FM audio from a recording\n\ngamutRF provides a tool to demodulate AM/FM audio from a recording as an example use case.\n\n* Use the ```freqxlator``` tool to make a new recording at no more than 1Msps and has the frequency to be demodulated centered.\n* Use the ```airspyfm``` tool to demodulate audio to a WAV file.\n\nFor example, to decode an FM recording which must be at the center frequency of a recording:\n\n```docker run -v /tmp:/tmp -ti iqtlabs/gamutrf-airspyfm -m fm -t filesource -c filename=/tmp/gamutrf_recording_gain70_1234_100000000Hz_2097152sps.raw,raw,format=FLOAT,srate=2097152 -F /tmp/out.wav```\n\nRun:\n\n```docker run -ti iqtlabs/gamutrf-airspyfm -h```\n\nTo view other options.\n\n## Scanner testing\n\nCurrently, the scanner ```gain``` and sigfinder ```threshold``` must be set manually for the general RF environment (e.g. noisy/many signals versus quiet/few signals).\nTo establish the correct values and to confirm the scanner is working, initiate a scan over the 2.2-2.6GHz range. As the 2.4GHz spectrum is very busy with legacy WiFi\nand BlueTooth, the probability of seeing signals is high. If in an environment without BlueTooth or WiFi, an alternative is the FM broadcast band (88MHz to 108MHz).\n\nTo begin, commence scanning with just the scanner and sigfinder containers:\n\n```\n$ VOL_PREFIX=/tmp FREQ_START=2.2e9 FREQ_END=2.6e9 docker-compose -f orchestrator.yml up gamutrf sigfinder\n```\n\nWatch for ```/tmp/fft.png``` to appear, which should contain strong signals similar to this example:\n\n![2.4G example](fft24test.png)\n\nIf no or only small peaks appear which are not marked as peaks, increase ```gain``` (e.g., from 40 to 45) until peaks are detected.\n\nIf no peaks appear still, check antenna cabling, or choose a different scan range where signals are expected in your environment.\n\nIf peaks appear but are consistently not marked, decrease ```theshold``` (e.g. -25 to -35). If too many peaks are detected (noise detected as peaks), raise ```threshold.```\n\n## Troubleshooting\n\n#### Containers won\'t start using Ettus SDRs\n\nYou may see ```[ERROR] [USB] USB open failed: insufficient permissions``` on initial startup with Ettus SDRs. These devices download firmware and switch USB identities when first powered up. Restart the affected container to work around this.\n\n#### "O"s or warnings about overflows in SDR containers\n\n* Ensure your hardware can support the I/Q sample rate you have configured (gamutRF has been tested on Pi4 at 20Msps, which is the default recording rate). Also ensure your recording medium (e.g. flash drive, USB hard disk) is not timing out or blocking.\n* If using a Pi4, make sure you are using active cooling and an adequate power supply (no CPU throttling), and you are using a "blue" USB3 port.\n',
    'author': 'cglewis',
    'author_email': 'clewis@iqt.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)

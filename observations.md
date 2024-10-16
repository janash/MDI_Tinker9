# Observations from Running MDI Tinker 9 on Chem AI

The base Docker image has been changed to `nvidia/cuda:12.3.1-devel-ubuntu22.04`.

I modified the `mdimechanic.yml` so that MDI would be installed. The lines below were commented out, but I uncommented them.

```yaml
    - pip3 install setuptools
    - pip3 install packaging
    - git clone https://github.com/MolSSI-MDI/MDI_Library.git
    - cd MDI_Library
    - pip3 install .
```

I built the development container with `mdimechanic build`.

I ran a "vanilla" Tinker 9 calculation with `mdimechanic run --name water`. The calculation ran successfully and produced te files `tinker.out`, `tinker.dyn`, and `tinker.arc` in `tests/water`.

I removed the files that were produced: `rm tests/water/tinker.arc tests/water/tinker.dyn tests/water/tinker.out`.

I ran a Tinker 9 calculation with the minimal driver by using `mdimechanic run --name driver`. 

* The file `tinker.out` was produced in `tests/water`
* Kinetic energy for the expected number of steps for the driver (20) was printed to the screen.
* `tinker.arc` and `tinker.dyn` were not produced.
* `tinker.out` ended abruptly:
```
Received command: >VELOCITIES
Received command: @COORDS
The integrator is on step: 14
Received command: <COORDS
Receiv
```

You can see `tinker.out` from the driver run [here](https://github.com/janash/MDI_Tinker9/blob/observations/tinker.out).
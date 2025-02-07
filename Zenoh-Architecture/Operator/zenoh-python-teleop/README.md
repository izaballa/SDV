# Requirements

## Eclipse zenoh-python
Mirar [zenoh-python](https://github.com/izaballa/SDV/tree/main/Zenoh-Architecture/Operator/zenoh-subscriber#readme).

## PyCDR2
The IDL (Interface Definition Language) part of the CycloneDDS package as standalone version, to support packages that need CDR (de)serialisation without the Cyclone DDS API.
PyCDR2 is the standalone version of ```cyclonedds.idl```. The documentation of [CycloneDDS](https://cyclonedds.io/docs/cyclonedds-python/latest/idl.html) still applies, you just have to replace ```cyclonedds.idl``` with ```pycdr2```.

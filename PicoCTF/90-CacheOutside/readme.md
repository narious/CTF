# Cache Me Outside!?



SEMENTATION FAULT (CORE DUMP)

> LD_PRELOAD=./libc.so.6 ./ld-2.27.so ./heapedit_patched
Segmentation fault (core dumped)

We are given the simple binary file heapedit, however it cannot run on linux 22.04 without some massaging.

We utulize pwninit to start the binary challange.., however.. segmentation dump..

### Investigating Segmentation Fault

> strace heapedit


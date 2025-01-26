# C++

## Komilátor

If your library name is say libxyz.so` and it is located on path say: `/home/user/myDir`

then to link it to your program:

```
g++ -L/home/user/myDir -lxyz myprog.cpp -o myprog
```

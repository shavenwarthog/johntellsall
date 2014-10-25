http://en.wikipedia.org/wiki/Fallacies_of_Distributed_Computing

NetCheck

https://www.usenix.org/conference/nsdi14/technical-sessions/presentation/zhuang


ptrace! http://linux.die.net/man/2/ptrace


latrace (dynamic linker) http://linux.die.net/man/1/latrace
- uses AUDIT (vs ptrace?)


$ latrace -A /bin/echo stud | egrep stud
stud
 1633       strcmp(s1 = "stud", s2 = "--help") [/lib/x86_64-linux-gnu/libc.so.6] {
 1633       strcmp(s1 = "stud", s2 = "--version") [/lib/x86_64-linux-gnu/libc.so.6] {
 1633       fputs_unlocked(s = "stud", stream = 0x7f36c69d0280) [/lib/x86_64-linux-gnu/libc.so.6] {


$ strace  /bin/echo stud 2>&1| egrep stud
execve("/bin/echo", ["/bin/echo", "stud"], [/* 66 vars */]) = 0
write(1, "stud\n", 5stud


XX ltrace vs latrace?

$ ltrace /bin/echo stud 2>&1 | egrep stud
strcmp("stud", "--help")                         = 70
strcmp("stud", "--version")                      = 70
fflush(0x7f1b8f013280stud


strace in 70 lines of C

https://blog.nelhage.com/2010/08/write-yourself-an-strace-in-70-lines-of-code/


strace+ writes stack traces in addition to each syscall

https://code.google.com/p/strace-plus/


truss: BSD-only


SystemTap

https://sourceware.org/systemtap/wiki/SystemtapOnDebian

Note: Default Debian kernel packages currently do not support UTRACE which is required for most functionality of SystemTap



http://www.slideshare.net/brendangregg/what-linux-can-learn-from-solaris-performance-and-viceversa


dtrace?


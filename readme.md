#Password Generators

These are some simple scripts for generating secure passwords, using
Unix's urandom device. Great for sysadmins!

##Installation

Just copy the source code for the script you want, grant execution
permissions with `chmod`, and move the source file into your
`/usr/local/bin` directory. Both implementations are basically identical,
but the Perl script seems to consistently run faster.

##Use

`pwgen [length] [number]`

The `length` argument is how long each password will be. The `number`
argument is the number of unique passwords (all the same length) to
generate. Note that `number` is optional; if left blank, only one password
will be generated.

For a simpler Bash implementation that only generates alphanumeric
passwords one at a time, see my
[genpasswd.sh](https://gist.github.com/emullis91/6fd551ccf7f2b797c401)
Gist.

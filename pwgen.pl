#!/usr/bin/perl

$maxlen = $ARGV[0];
if ($#ARGV > 0) {
    $numpws = $ARGV[1];
} else {
    $numpws = 1;
}

open(SRC, "</dev/urandom") or die "`urandom` not found.";

for($pwcount = 0; $pwcount < $numpws; $pwcount++) {
    $pw = "";
    while (length($pw) < $maxlen) {
        $c = getc SRC;
        if ($c =~ m/[\w\Q!@$&*?\E]/) {
            $pw = $pw . $c;
        }
    }
    print "$pw\n";
}

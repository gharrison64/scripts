#!/usr/bin/env perl
use File::Find::Rule;
($location,$dest) = @ARGV;
my @files = File::Find::Rule->file()
                            ->name( '*.ipa' )
                            ->in( $location );

for my $file (@files) {
    print "Found file: $file\n\n";
    $result = rename($file,$dest) or die "Cannot rename $file to $dest:$!\n";
    print "Moving of $file to $dest was successful\n\n" if $result == 1;
}

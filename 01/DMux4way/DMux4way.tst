load DMux4way.hdl,
output-file DMux4way.out,
compare-to DMux4way.cmp,
output-list in%B3.1.3 sel%B2.2.2 a%B3.1.3 b%B3.1.3 c%B3.1.3 d%B3.1.3;

set in 0, set sel %B00, eval, output;
set in 0, set sel %B01, eval, output;
set in 0, set sel %B10, eval, output;
set in 0, set sel %B11, eval, output;
set in 1, set sel %B00, eval, output;
set in 1, set sel %B01, eval, output;
set in 1, set sel %B10, eval, output;
set in 1, set sel %B11, eval, output;
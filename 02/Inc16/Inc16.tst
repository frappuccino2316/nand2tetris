load Inc16.hdl,
output-file Inc16.out,
compare-to Inc16.cmp,
output-list in%B1.16.1 out%B1.16.1;

set in %B0000000000000000, eval, output;
set in %B0000000000000001, eval, output;
set in %B0000000011111111, eval, output;
set in %B0101010101010101, eval, output;
set in %B1010101010101010, eval, output;
set in %B1111111111111111, eval, output;
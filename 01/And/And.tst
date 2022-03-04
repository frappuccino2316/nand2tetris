load And.hdl,
output-file And.out,
compare-to And.cmp,
output-list a%B3.1.3 b%B3.1.3 out%B3.1.3;

set a 0, b 0, eval, output;
set a 0, b 1, eval, output;
set a 1, b 0, eval, output;
set a 1, b 1, eval, output;

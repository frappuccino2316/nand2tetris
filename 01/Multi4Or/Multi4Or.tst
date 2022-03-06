load Multi4Or.hdl,
output-file Multi4Or.out,
compare-to Multi4Or.cmp,
output-list a%B1.1.1 b%B1.1.1 c%B1.1.1 d%B1.1.1 out%B2.1.2;

set a 0, set b 0, set c 0, set d 0, eval, output;
set a 1, set b 0, set c 0, set d 0, eval, output;
set a 0, set b 1, set c 0, set d 0, eval, output;
set a 0, set b 0, set c 1, set d 0, eval, output;
set a 0, set b 0, set c 0, set d 1, eval, output;
set a 1, set b 0, set c 0, set d 1, eval, output;
set a 0, set b 1, set c 1, set d 0, eval, output;
set a 1, set b 1, set c 1, set d 0, eval, output;
set a 0, set b 1, set c 1, set d 1, eval, output;
set a 1, set b 1, set c 1, set d 1, eval, output;
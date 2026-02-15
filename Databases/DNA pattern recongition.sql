/* 
+---------------------------
| Column name | Type       |
+--------------------------+
| sample_id   | int        |
| dna_sequence| varchar.   |
| species.    | varchar    |
+--------------------------+

sample_id is the unique key for this table. Each row contains a DNA sequence represented as a string of characters
(A, T, G, C) and the species it was collected from.

Biologists are studying basic patterns in DNA sequences. Write a sollution to identify sample_id with the following patterns:
- sequences that start with ATG (a common start codon)
- sequences that end with either TAA, TAG, or TGA (stop codons)
- sequences containing the motif ATAT (a simple repeated pattern)
- sequences that have at least 3 consecutive G (like GGG or GGGG)
Return the result table ordered by sample_id in ascending order.

*/

SELECT
    *,
    dna_sequence regexp '^ATG' as has_start,
    dna_sequence regexp 'TAA$|TAG$|TGA$' as has_stop,
    dna_sequence regexp 'ATAT' as has_atat,
    dna_sequence regexp 'GGG' as has_ggg
from Samples
order by sample_id;
### Testing results.

Tests made throughout development are summarised below to validate the effectiveness of various changes made throughout development and their improvement on accuracy are .
Note that no time trials were attempted until a satisfactory level of accuracy was reached.

It should be noted that intrinsic to the algorithm is a random shuffle of the training set, consequently, results can vary by approximately a percent between trials.


| N pix   | Threshold | Smoothing kernel  |Flare # correct | Good # correct | Comment  |
| ------- |:---------:| :-----------------:| :------------: |:-------------:|:----------------------------|
|  32     |     -     |           -        |    20 / 40     |     40 / 40   | First attempt               |
|  32     |     -     |           -        |    36 / 40     |     40 / 40   | Adjust training/test ratio: 60/40 -> 70/30  |
|  64     |     -     |           -        |    33 / 40     |     40 / 40   | incr. Npix 32-> 64          |
| 128     |     -     |           -        |    33 / 40     |     40 / 40   | very slow, need filtering   |
|  64     |    100    |           -        |    36 / 40     |     40 / 40   | thresholding added          |
|  64     |    100    |           3        |    30 / 40     |     40 / 40   |                             |
|  64     |    100    |           5        |    28 / 40     |     40 / 40   |                             |
|  64     |    150    |           3        |    39 / 40     |     34 / 40   |                             |
|  128    |    150    |           3        |    39 / 40     |     36 / 40   |                             |
|  128    |    200    |           3        |    40 / 40     |     36 / 40   |                             |
|  128    |    200    |           3        |    40 / 40     |     39 / 40   |  Incorporate shuffle        |
|  64     |    200    |           3        |    40 / 40     |     36 / 40   |  incl. shuffle.             |
|  256    |    200    |           3        |    40 / 40     |     40 / 40   |  18 hrs to train..          |




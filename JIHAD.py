# Encoded By : MUMIT ISLAM HIMU
# Encryption : Py3 Marshal+Zlib+B64
# Github: https://github.com/MUMIT-404-CYBER
#----------------------------------------------

import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'eJztvQl8U9mZJ3qvdskbmM3YYC4GYxuwrcWSZSgW7zZ4A28gY4wsXduyZclcSQaETEyFdFEJSaCKqqIWGqeSTlGdpFMzPT2TmemlUkk6mdczPRKjeeXcN+5JZyYzU7O8cU1Sr3met33f3Y5kGwqSVFIvPxt9//P9v7Mv9+iec48u/45K+dsouT+/n0VRr1Beykv7qUnaRdOoq/yUS3RVLpXgql1qwdW4NIKrdWkFV+fSqShW71V/naaob9By8jQFVt24QeZezSr+eq/2l4hFjRsVf93H+OtXzdXwMbkaPyZV03J/Y3qbmVwmwc1wZchtJLiZrkzBzXJlCW62K1twc1w5grvOtU5w17vWg5vhX9eD6WX6cyc3uDbSVKB8F8Vu2k1xu1aUKOtp2+k0FdAJqL6oPk1doG/S3qOuzRAra3yLHGqU8m54k06P6coD68ZbtHcTyGaQLSB5IFtB8kEKQLaBbAcpBNkBwoDsBCkC2QWyG6QYZA9ICUgpSBnIXpB9IPtBykEqQCpBzCAWECuIDaQKxA7iAKkGcYLUgBwAOQjyDMghkMMgR0COgtSC1IHUgzSANII0gTSDtIC0ghwDOQ7SBtIO0gHSCdIFcgLkJEg3SA9IL0gfSD/IKZDTIC6QAZAzIIMgZ0GGQM6BuEGGQTwgXhAWZARkFGQMxAcyDjIB4geZBAmABEGmQM6DcCAhkDBIBGQa5ALIRZBLIFGQyyAxkBmQKyCfAZkFuQryLMhnQa6BfA7k90CeA7kO8jzI50G+AHID5IsgXwL5MshNkFsgL4C8CHIb5CWQl0FeAbkD8irIayCvg7wBchfk90HugcyBfAXkTZCvgnwN5A9Avg7yFsh9kLdB/hDkGyDfBPkWyB+BfBvkHZC/B/L3Qf4Y5B+A/AnIPwT5RyDfAfnHIP8E5J+C/CnIn4H8OchfgLwL8l2Q90C+B/J9kB+A/CXID0F+BPLPQP4XkL8C+ecg/wLkr0H+JUgcJAHyAORfgSRB/jXI/wryPsg8yI9BeJD/DeTfgCyA/A3IvwX5CcjfgvwU5N+B/HuQn4H8B5D/CPKfQD4A+c8g/wXkv4L8N5D/HeS/gyyCfAjyP0B+DvILkI9A/g+QvwN5CPJ/giyB/E+Q/wvk/wb5f0D+31t4bVMC0gKqBFQLqBFQK6BOQL2ABgGNApoEzBAwU8AsAbNv0Scp11bQclz5gOtcBYDrXdsAc13bRylXoSQ7wLIBZKOPdjGSvilF34w6zD07Qd+SPt80UINzriKw57l2LZ+dwLp1xfy0G6z5ELKYzUv3eZ26q3LtAd8CV4mQUqnsAzYs8/avqyC8SkmpDGyFrr0rwmJtmGVh960IhXUpWhZqP9h2ucrZXa9jiN3sbsEtZvcI7h625HWKLRP0Enav5O6T3P1SnHKoxzpXBVs4V0mt8sdWLJ/pb3zlkS37r1xmsJc+RcuWufasEnbvirCWFe2xD2T/svawPlFaNrCW/1b7rGL1PmMtIFYQ21P23wZX1SP7r2pF/yU/pv8qn6L/zL+l/rP8VvvP+qnuP9tT9F/Vb6n/7L/V/nP8dvsP4lVfo1x2cJ0uB2ANsGpwD4Dr9FLumlHKfQDkIHzXPQNyCOQw+B8E/yPgPgPuUXAPgVsL7mFw68A9Am49tIL965DTNyiSJ9iOLLd5Vd1UaS0U7APkZTSvmXKHxzoiJcAGCgYsB23WyZ++8aKgVU8OMvVjrIdpCnJM75TXHWaZnTuZUTGth0ci+x8Rqd/tC6dG6gkG/RgzahgFj6mI389rPX7WzUWGIYWCAZvzoP2gzTZpWrz76pdBPi/JcyBfYgBugnxh8e6dvwD5UynQLHp8SfS88+eivDor2VCuShGfM32AAyFqv+gdLQ9OsQFmLByeCh2orBxxe9jhYHCiwhOcrBzlgpGpUGW11VHjsFmrnbYqu9lir4QmovcC5PaMcazb2wVVabzIeiLhIBfdN+WbYnyBUNjt9zMcez7ChsIhZiQSjnBs6NAhK3OYqfSy05UBqPHSFsikQsnR7Q1NugPuUZZbWp/m4feF2WWmIOdxL21IM024wxB7KTfNOIlxS2egc5f0zT3lFii+pFjNkmJTFNmrSrZUyRa7ZLHKXlWKAl4GVJyWGlmzOqxLRtRqzA5zq2isMTutimaTNEhY1uyyr6VG1mxmKcEau1ksiNUsmVAxy6aQoNjQgrlWWapOdXYJNkeNxSko1WaLWVKssmKTlSpZkWpZbTEril1S5OhW2WK1iCWphiY5KZmk5qq2mW2SIkezWRVFDmN1SIqcfZXZHs1FxW43MwxjB9VplrJzYvm1qFiWdIIjRnLKJXRapPI4rVZzt2iqkgIJDSkqUAydoDQLgWuFqgoatLF5yYRaR8PJztYGwVpnrZaSrbPbbGLzClodUduWsmXVdby2taNXCm9XYtotVkmrtkpateJbTWxO2QajQdZsTqeg1dvMkm+9TR5e9TZo35OS0WYhRutJRbX1yP5Wxd9q9UlGu9UsGUFrlY3SAETNLmnV0uCtd1RL+TRarE6rmHijxS61YiM0PtGssmZXbHbZ5pAGK2h2a79otMljqhHaskb0Rq2VqGKGzXabuSWK2miN2Twi2qCXmwStpUYuTiuMJKekwQgSNUeVlEurE5s5W9Qc5s7jbT1dtYS7+tt6enqkkFa7UyhEK17bDVHJ6HBKGl6fYkQoWV1tbV1Pbypvq2/pTOOYsJgclLBRSMTnrJZL7ayWLsTWGqmVUHG2ieFq8HqVjE5zo6Ja68UsUG3sFwai4uWTVBjtzVIoUNuOQ8F6iFc7UbuI2qNEsPfCtVGnRLA6G4naStQ+WbU7u4iqWB0kbI2VqPYWoraJ7VCDA0c0wozSqqj2DkVV0oIeaCbqKUWt7pPSggEXxTadlKfpdrvDLpl8AbGBOmDgwORhEFR5ZkDNLmsWxSZdOR3QazAbGCTVLhmFdjNIqlXRiLedeDsVo1OcdTqc8jTfIUyAkmZRbFZJq1HC1cgjsAtyNtf3157qrhWSFXg7UcVsQbWI5e+CKUQqP6p2RXPKmpRtl9IgXXa8yDNEzWI+1WCRzVK5uhxWadwKWptitMiaRQlokW1OOXVlSu6qtsnJoFYnGy2Kt1X2hn5rIGp7VFFPErUvapBUi6xZRK3bBlOLolkVzSZr1bKv3eKUNbAZBQ0Glk8y4oCSjHZbv6RWV5uPE7VdUqG6/VIs6E9Zs0sZYVOKAVE7qRitsmZTvG3mfkW19QhqCNULclCSpl2sEHg7FJuTaFY5HaetTjbWyDlCB0jeoLUpRotitNQRlfhbFaO1TjHaFKOSEXSqbLSY64haT9RGojYTtZWobURtJ2qHkoNSFouV5GAlOViVYsujwQ6dK3s7SLEcJCuHuUcJalO0akWrkTWnkpDT3CAZYVDKmpIPaD5ZrVayBLWVqHI57dXSaLQ7lJQcZrkYDqVJQTuuGC2yZlWiVCsBMcdsWW05XufqqZUD1SiBapQB6VSGIWgNRG0mqo+obURtJ2oPUfsU1eJTcnAqxhrJ6IC5SywlanV1+G2r+EidjJo0tqD2stFilnveYa2RLpZuhzDismXV1V/b3ir1kEMZNA68k5KNdumicNjliwK1BqJKHeSolhsNtTaidiiqPOZw+pPKAFrL8dpTTbWKj5ydU+5R1OqI2kjUNqK2y+mBWlfb3XiSeHUpCVoVo5UkKF8TqPqUoE7F6JQ6qhomn0ZFtSmqXR7hsG60ypo8yFBrU4xWxShnCqrc0qA6FaNT6uNqm9yoqDUTtU3xtypGuXlx/hebA7VaccikcritSeU9PW1dhMPXKfobZd5GVLmkygWMWrtitCpGpXqg+oiqlM/hUDSn4u1slY1KQ8F9bKOiKg1ld56SNXnGrq6WRwtqcj7OGjl10KTUnco8hHenkuaQh3YPrEZqhNukHkuVWVLgOwWXUX1Ot+SKw6SvXh4mfe0Qq1sI3W+xWSQFvoBQOeWULKeciqXaLCk1YglO400wl0VRFJeNkIOwDmE9Qi7CBgR82s5tQtiMgFtuXB7CVoR8hAKEbQjbEQoRdiAwCDsRihB2IexGKEbYg4B7QBzupHFlCHsR9iHgPg9XjlCBgFtenBnBgmBFsCFUIdgRHAjVCE6EGtx/WdcsrXfl1S53AP0OIjyDcAjhMMIRhKMItQh1CPUIDQiNCE0IzQgtCK0IxxCOI7QhtCN0IHQidCGcQDiJ0I3Qg9CL0IfQj3AK4TSCC2EA4QzCIMJZhCGEcwhuBNzF4jwIXgQWYQQBt8q4MQQfwjjCBIIfYRIhgBBEmEI4j8AhhBDCCBGEaYQLCBflxhRWZc3Smoy7hH5RhMsIMYQZhCsIn0GYRbiK8CzCZxGuIXwO4fcQnkO4jvA8wucRvoBwA+GLCF9C+DIWQlxtWKRhLCxyuJvoewvhBYQXSTj5tkrQWhXV0srdxpAvIbxMgsOVyr2CtjsIryK8hvA6whsIdxF+H+EewhzCVxDelFMRFifcV9H2NYQ/QMAtUe4thPsIbyP8IQLuk3LfRPgWwh8hfBvhHYS/h/D3Ef4Y4R8g/AnCP0T4R3KWXbhw4r5DKCwAuH+MQf4Jwj9F+FOEP0P4c4S/QHgX4bsI7yF8D+H7CD9A+EuEHwLw+u7a9u7ejmZe09Z+uorXIVb38br29jprzXHJbQf7yVNWa73kQuiO9iYrr0N0nIrqRfcgGE421MAkrhfdg1FDd1dLeVu11czrWtvbqquOo9te7WjgtccaTthqeN2x7m6L/Ri4rk47eGuOd/ZAMRBrWqIZ6Ha3l/fA3QUYe3qdVfAFDIZa6M6mqFHWehVji6A1223WJlGrwYCiZlU0G2h6UbNLJrvkecxmlVIWtA7F2KJo7aI3rOpk72qzRYzdAZl0C0n3WOB+UVBwxSEpisUuKU7JyyYHtlkkL1hzSIocyy7HsttlxSF5VZsli1NRoMm1wsY0rxv1hcciw7yuyc35Lrl53eSwO+TzLJkiIZYrd4+ygXD0h+3BqM/vd1faK8xM6SmL5SDT5gtELjIXnY4hR1UZUzs15Wf72eHjvnCl3VZdYXMwpcdbetrb9jN+3wTLNLOeiWAZUz/GBSfZSovZVmHGf0y3ewRylaMMNNXVdlQ21bV2dh9sqmvoq/R1jQUDrMW63wK8vUHioHd3VPqEQN19lRZbRVUFBujurrSC09pQOSUFa6uvZANDvRiws6vSPujeRlNUg9s/7ZuotFZYsDJCPQ4yvQeZ2oCXC/q8DNZO6Cuno4Opi/j83krXcbgjsJcpBayqhRRr+yprqmsqrBUg5ooaJxahq6NylZ3z9JLU9VU6nNVWS3V1FUapP1nZ7A8y7cFhnx/L3N5UGXJPhiKBUQzbkEKgQeRySTUX4tdWQi8ccHOTrHvYVz5djdk1tFde9rKBkC986ZC1wr7/gs8bHjtkMTvN+8dY3+hY+BAsec0zEHKoqb/SDO7JPnAGo/8sraelxpFbpuYg0xGc8LmZeqvUMF1dJy0VFqcZFgAVZmy4C9NPPBj6WC7kCwYqqyAnZWDgsKhy1jgqqmukJkkfI2IPNLbXKm3aXCf2hbWmWhhUMBwsFtvBQd86uMOINj+uPhazXCEL0+WPhKRKneiy1FbA90y1BUaI1SxUqkzP0w6eruZpJ0/X8CqYcFQWCwjcFDI9beVh/0Em2vyr1BwKWGG31Nih5h/g/cUH+O3O02bfGNyc+XbDLdkHeLf0gfCldehJ2iY01Ngtto3NUiO0TXWFxVx9cHCJZqIqKK+qjFmiK6J1v3qfR/MfHb4sn6drebqOp+t5uoGnG3m6iaebebqFp1t5+hhPH+fpNp5u5+kOnu7k6S6ePsHTJ3m6m6d7eLqXp/t4up+nT/H0aZ52fYAPOn3/UY29+2saatHDv9pYizrSmlCappj6rl5G1JnObsbiGDKLpWp3e9Bwqiz6sUGipalVdMAogba3r1bJaFCsQ6XVXIt7LqOPnE5tj59OHRVmcTK1rZhMPaGhepc8mUZbH3ttWchAMKdeXSfx6rKaof0hmlkaPlW/TLRoy6/S/fgVZDc7oBOtNU90PYXdQ60d0vVkswj9XwPXk/3gIN6MK39aEBib1M9vaPCQcpgmXmE10ceV4wLpD83TH+U/MraiPy423p/PUF56TkOt8hdbFnqGDmek5KCTNa8qPdy4XomhSisTOYy84mB1eAMJt/KAdJqvNkZHV9RkWZgVR4PTfFccoH5EKVccqQ5vSgmntMXKo9Vpua1ysPqp21Edo2PqaVgHpqWc8YTly1wR7lcaczOaR+Sz4sC2l+pOb4vsx7ZUzmN91/3SvbF6764P5xH765Q39676ESPrSfMpSAmXLWsrjrxAm+x64tDhwpQW2DAh9A9XnNouYYboK0q0K8VvWcqnhZKIKB6XL9vYEcGm+ttv/3m0Vj6UIt78C0dS2sfKj/nG3N4qc1XlMUtLbYP0VznsDw5XTrp9gUqYb7ngNFsRvhiO6hjxUA1noiijSTpWU+WY/OnL18UPA38pRFHTDQxRHhFi1VirZbgizoosfkm+IrNVc1lZ2l/O+gTZL2uyT66eDPOrJrp6n5cKA4ypC3aHykxytpYayPel2z996eaTfV5hGFLgxXtf/8JPP3tv8e4rL4G8CfJ1lJ++8Uc//exdBtS7IG8s3r35HMgsyGcX7167h37ML5n98tKkV+MWKdrA4r3bfzKYUlSxALdBXpQK9CWQW8yyotz6JOp3K60c10BuYN5SpC8yqX8pER9TubuvzqZX7nNSYs9KGVyVKojy+d98HdPrl9LgL0iCHtdJ5Z+01tfTa/1ySrleTEn5yyi/8VrfewUE0rsH2d+Dyt6DIt27LdlRf0HSX5b4S09V9y+m1/33pBaUhzMO7avMp2I8S+PwjjQOrwkXmlT3V6R2eFmo/xPW/c6fptf9RSnVL0ju76Vkf+N3rd+fT6/7dam5v7RywvitVhYreUvit6Rw6N56isqumLM/J3Xsl8SO/YSqm5Ims3x0X5VHtTTMvkAiC0MPp5znPnbyfu2Jv9LufhI9+OTZLy9NwYDZPCkc+zZPRnNPByMcc5y9xBxgpEPh0RLpTHjPmC8kHgNvDTFdbp+X6Q4ydZdYpmcMj4f7o5u72YCXUVLoH3OHQ3BvGz244tD2hQsXKtIObruH2dFhN9wRu0PuilTC6eHOPLpVKgKeZD/Wivc4ci7RcqmY9cHAKOcOR/zusC8YCDE7SUGguNIttpfDfQTp8PtPjkStaXVq4liWqYuEMSbTwbJe8GFqPR42BGHkgNFNSrodwbCScHS7UHk046H5FbGMShtEt2MDuCsm2cp9TqfZ4jCbrXabrcZ5JMxeDB/iDUNDuCoYGirL5dWhMMergiFeP8qG2YjPyxtA8QdHfQFeMx4ENMhH1nk1+PAaTIPXhS6Fwuwkr53ifAE0+iZZXhvys+wUrw67A5DupRCvYS/6wDPgBk8NpBnk1wttW9vWX3u6u7OjqfVkY5mW10QwXxWILsRy0yzHG7Ab691jYV49GRoNYZMK18ZSZmtHR2d9Y0cPU9d5miuAnhMAH62G/icos9SCMfOLJ2+4nj9z40zCmJ805t/t/oPcrxV8ZfvXtie2Vya3VyaMlbO75/WZz0Wfjd7cndBvSeq3zBYtZGy48Uw870wiYzCJn+HZPR8ZKLX2Wtn11oRqc1K1Oa7avKDSL1I5Rlb9IZWjHlH/QsBFAT9iKLUhbtgxp0oYihKqXUnVrrhqF0SIG6oSKntSZY+r7AJlEqqdSdXOuGrngkpzrSyeCekfS6qOxVXHFlS6a3uvn7hafq18tlwIvCehKkmqSuKqkkVVrnrrQs6WG7H4tnOJHHcSPyOzLfN64/VTs1dmryzoMuKZhxO6I0ndkbjuyA803zf9yPLdrO9nvZu1kJnzkuq26Vbm7cxE5vZk5vZZz4LOdG385oarwWvB2eC8zjTr/RnGr03o6pK6uriuTkhud0JXnNQVx3XFAt2f0JUndeVxXfm3wt+Mfmfn2zPfnLk/s6AzXPPF1x2+Ww8gfr7DJdalJoV5rb86eW1ydnJBZ7w2dnX82vis8O/hokoD9dLor7VcPXbt2OyxBX3G9egD/da4fuuC1vTFqqsD1wZmBxa0mxPavKQ2L57yWdRShvy4EPThw4ch3A743sHaquaD1A8sdQZwfniwVtWqVkfeMFLU2kp3baW7Ol+9z9dWup+Cla7YB79jS9v2WqhUK9NS213bwYj3Gr8r61ezxelw2GssTov1yP//16UpG6tHfhdWmb9073yaVo8Xlb+nqcPaovDTvChMew6rluTneO40/Tmsl17tSVaZqiOyQ42/EIbELHBf8E1pLbdmWDOsGWRDGc1tgCvnbernwsPKnaDzWr8vwF7kikHHQ68hPCsOS2hDVjx7b8KwL2nYF5c/3G4ItPqF2rfiQh1X9JWXbFib8pBUR/RHXNocnoEo03AZuNbPRcBacPkIuxCwXEJthJAC4LHd0E6pLqYbxpulCUNB0lAQNxRA3b7ofT7jRsZ14d/KWhnkWhl0y2u14iFwygPsVeqZ6qt6rO/KYxcpbbT82MUMFaO82mmK2xjWk1DjylGRlYcsILx+mrqp4l57bG1S8zQsP2KSfjgiRnuN6e/OmEvpyUflMaf/+DAzKnzzXHgd8d9Nccyy9lpxdCP1wfvKB+oBzQXpUXpaKiuPaaS2wLLDGTPqUWpGY0w7dJAWftkhi2WxtQEjHi7wZs9oyXvw0kqz8pDFFuIbW/buwgZqcN+MLqaZy6RW+Usr17qYzpuNxydep7zr76ofV0qaurE/rUy5T9VC+pjeuwHGZUE4n4RavYTejctTDuQ/QaxNK8qzPcV38zeXvfXGTs0YHjvidxC/8E6ix1SP7UtjWhvlxYzYut6tMTW0cP5d9apHVVJjFDzNcZCYCvr6qzOmmGkud9U22Zae2hm4ImcyZjJjmpmsmNq7HfqjMGaY27Ba3HAp0WMZscxY1tdhFvmGMpPAeDgMaWgfm8bej03jHKRR+Ng09n9sGs9CGjsgje2PTKPiY9P4mvDmTPiXPnPJR38sVEhzQSVemThr0JKP8D3EdETwpzWM/B6bWnIrPYi3y6+Kt8uv4B31HTS8LBG8tf6K5Inua8zAETnCfSnMPXxHzQvS22xgOfAqLAdevYbrLpBnB5kIm5q1ZVnWd6VchBzQ8BbI63I5MJ/bUnnupNzuo/w+BviqFOA1DBDZQ3KyTJqX5YTxvyHl9FbElloo4b0+aYFflkohF00oAHOAKVPxtJVXma3RdVOXwmPBAHOytqOhs71i6lKZlvtvkCh4Wrh/D4rIaHdkbEVW0iuEpPJjQ761ajfIXfCyVMu3pABCt5Ak735bSZKnueh+xeeUYhc3avxBj/D0R3gy0xSMBLxM5Kt0SptZUss2JzXaWylt8QpD+lEIqeQlRcDifYORlFdwVaYkaVKysT5xNtZHZJPamdg6bzKt3tAqOdmeOCfbKjnJw/4VSb/9cRWreuLsqlbJ7iUhwKpZMJHCR42i+rGgz8PC2Iy0pwY5ogRoCV5g2t2BS0yXOxS6EOS8IaYhKDzD63cHwsIzPK+XJH3vbSWm8HAxciwt59k3Fe/Gi+7JKT8rPQl1TI74uFCY8btD4f2ghkOyFgpbrDZGihYpelRFuiJhZkoqIhPB34GuNsKj1lWqKNeHhfp0j0F967uY1oYQU3qpMlAGV62WpwPcknB1BoK8qqOTK8Vb7nJcRdCXPsC2LaP5jEn3xSHIfYLlQtE8aJiw249PKuFCCac87y2ADpdybmdhDvASv/aoXvKJ7pMahekNsUyTH3/9wrQHvazw+LN7Cp+e9k5JgZfoGE4sFm4vFAg1G8wiNlSqQKkqyxMXBxuERY8vMBUJkwUFr8GnprwGX9zFm0JTfl8Yl0UhPle45uFKFy70Ro4LclweRlDjM08t5w6MsrzOPQWxvbx6yjPFa8Ic6+VMQhg/GxAWVrxWSJLXhSLDk+CqJi0gMAVOQhknq8qyAVleK+TFq0aCvGYyPObltRApFOYNU6Ehvw/j0T5e5bnIZ3o4t2diSErMGMYmHvJ5Q7wGf/cFRQNVi09cQxAXxgKmEsJzrGnb6Iy4YjouA/5YMXRXLayYaN3VLde2zG75Ga1bhPVQs+pDilK1qH4h4KKAECaujyTo6SQ9HaenBepI0NVJujpOVy9ojHFTU0LTnNQ0z+bOa3TX98U1m+CzoNVfOx3P2ZnQFiW1RXFt0aKB0urjpqK4piihKVpQ6a+WXCuZLVkw5UA+61sw54xWzBlwthgfFZoWDJnXe2/ans+5kfO+YdsDw7aEoTBpKHzfUPbAUCauWWets9aHC8aCRUqlNhFYUBvixsMJ9ZGk+khcfWRBrb/quOaYFf4taiHAw4cPP9JRagPkbYzqIW/1Zf0vBFwUcEGfGc+qSujtSb19dve8wYRFUqtzFrLXv1QczwsnciPJ3EgiezqZPT3rnHU+XFTR6pz5rGwkQB8+FJ7puhOq4aRqOK4aXshYdzPv+SM3jixStNpDizjrnlcbnnvm2Wde0sY3n3t3/buW724ARfwk1rmT69wJ9XBSPRwXPkKS9QlVQ1LVEFc1LGhN8QxrQmtLam2zRfPQuhnY0PBZUOueO/DsgevehHpDUr0hLnx+tsK4oM+4o4rrCxL6gqQemnCd2nwnBk13tfpa9Wz1Qk7uS7ab3K3q29XPx27EZmuERi25b0wYLXHraLx/AFH4JIyjCfVYUj0WV48JoQ4l1IeT6sNx9WElufmc9YuUSWMWYDY8v27jK6YXTHdst3Ju51xtna2/rp3P2YjPuDOuR8UHvfPa9e9r8x5o8+7m3qmf086NJbSVSW1lXPjMG7Nu5seNBfD5zYV7uLgJa5AFDSW0lgAfIvyCSrM9EmBgfEwoC6XdBddICH9J/56uqu4g9d7Bkvpi9fd204DfN25r2EN9f4+mYb/6h0yD/rhd/Vd2zfEa/V89QwN6UhYfZHvjil7Y3kjxIps2cypqlT8vnbpdEzam6Caipy9HRlRR3SrLodVzfYItBIibkxLXsHqoGbWRitFzKSVMqcWyxZ1XvZXE0zxFPE1KPHl5r01d3sPy3LRaSsvKqotpnyicHpeCN1WDb88YYBGUsVoMry6mWbYts3o4fUz7ROEMMd0ThTPG9OnhYJFMmocaz5K18LaU+qUvq00+ymvyZrxIezO9WYDZ3hzAdd71gLneDYAbvZsAN3u3AOYJuDVmAsz3FgBu824HLPTuAGSEWDu9RYC7vLsBi717XqRnMmLquZTxk1KDkhhukJQu3yCZyUzdGBhfr4QvCxcTeyxzXFmULts6SG+9jdQqf8s3+B6R495PLscY5d3n3R8zesvf0OG2wdymVWNVxLK8lbGMb5rTl9Yz2TH1+GYlxy2rxV22EZj38WFmcryWWA4s+f/saVOfWee1zm1dLZzXdo166rLmf3yYhsf/Lmt9uDqlDFUxKmZ8xLxYkxLO7nUs68tVZ2Xou2rccpK2oZyrbj+lzC9z21ckQa38TSFufgTC3hqhBwLeA+FnSFiweNJqdDAm/GLR+0xKOQ6tWo7U+h3+Ndbv8C9VPw2I6qbqxjcCFbuocDYJPc4omnIt7qa4LZBTY0ooZdvOe2SV//KEbDqnfK95NVGYC91qYVPpaMdH58CWlaWsZIVFwKC8GiQrRaY4tIqx8/gqRnlpV6ws5rn/Aplw2LjCapTX1o5NsrDAaMJ1Ja9pgzUmrx0RCS44eU1LMBReyp5MO0C7lD3tYy9MBblwufBSAl5d4zQvGUOsp9wzVh5xL9UVicdVD9bBwshbdHD6UFFNTdF+pkj45a4vMimYLGYL2pqDwVE/K/2oV/FYWqckVz4p/LB3SXXEspRLrFN+d3gkyE0uGYv6fQFv8EKoaKlA8p7i2BFYd5Z7gv4gVx7yjLG4rhLWjbzaGwhzVVD7pa2RqVHO7WXLfQGIF+HYcvl8K/c30ESwnvN42Knw0t/gOdfKsfCkfz+s8Pw+cd+n8iJa9l1cbp30Hzx/yFxRs9836R5lK93TvhFJvcAOT8nWqcDo/r0DmDEXhtXr8CXGI26BhYOMexp/Rg0NPYlLcI8/CIEGK58ocCjs5sKDe4USONPKFfKNBlhvOXvRM4aLVWjnYZtY0KVsbLURNgwNF/KFWV4TCAbYVOskLLV5QwCqMuoOp/ngQjOVe1lcqHqDnggWZylHbMFyNuAJen2B0aX1o1Hf1H7Gy45A77H7mWFOCeOHYkWgbZay2UB5b/d+NiAWL+qUD3JPpR/jFk4m4+uyfR62fNgdYr2V8o5H5ZGIz3toqWzPiD944ZAQcCgQHJryBfbAyAhxnkNeFsYINA3r3TPEebmlPFwnHyryh7xFzLTbHwG9tGLvkbKipW2iz7g7GoTKLfONlj22cCH3NFsulrCSz0wtx9s6Xg2Z8XopXV6NB581ATxRrcFS43vWQ6Fo/ZNXHgrmw7enl5NWCI0N+w+Zm95W8xrwcfM5bj8kPcSxXh/UPhzi9WMsXABciNd5hoS+pA96Uh6TCL+Ex7uLn+NG0yvUKMyeg5nCgwV6RhWjX6e9VEz1On1XfUt1I6ubepteog8Jz2IhS1WFmVdPsJd4rdBkIVxryNsNS6ZncDcCajJ1OLp50lLxDG6n+kOHK4jdCOF+jl82sxQsuqvqVamY6HLFu7rjva531cK/3nd74/bjK8MJT3U/OkbmVqs8t66YLyXvzuODq86xcuziUAR/F1wZ8nrc0MZCWhCq8zhAuwV/V8vtw70UG1aTNvEmmH08E1NBH0w7ZixMgVQYYY/canbKBYL49V2DzEfCEXcgzJKw/1VTPfnR5lUyrO/CvD7Au7q3d+MXEkxYobA3GIEp/AInXMf+YHCKqxe2oIITIZjZ/ZHQGJdDC2+FYkP4QgWuQfgegFHBcryeY2FW9bC8Duft4CSMCmE/lNdERtkAtw6DqjgWz+a7Oc+YsLvFrRcSEF6GD2MWvi54vQdGqQ93nUbZ8JDX54EhDeMgxGWLe25hdjIkPro/gHAUoVYopWcqxJtgioL5AH9XwefUBwMBGKhAxD23jRh2E46vXK4X9T6EfqFGIalGg2g6K5QVklNPhaxwRfkmOFDdIV4VcfMaHPW8Tvx1A6/zefGK4Q046vxsmBW2wXiNByoBBY9M+EK51PJNM7Jx1iQDHqYIXdXieP2ZIeOG6X1D3gNDHgzDfJfqI3wcdw4dt8qLDqsawy0tt8qHe1roQMAB1Tga8wU0TqAP4KKAEMevCqLJr5pW/R06MdX/EJ0P0bki+l3B8Ogs5OYnc4sSubuTubuv6xdVu4075vO238t4LWOuIZFXlswru78zmbf/pnZRpV5fMr9j973Lr12+X5XYYU7uML+zPrnDdkdzR4MbV+i7BwnQhw/nN+W/MvDCwK3B24M3VfOb818Zf2H8lv+2/6Z6ftvuRSp/fdmHCDcb5guL7vlf8993vtOYKDyQLDzwfmHdg8K6d6t/VJUo7EoWdr1feOpB4an4aXd82JsoZJOF7PuFkw8KJ+OBSHz6UqIwmiyM3lEvFOx849C3NiYKKpIFFXdUiyqKOZ8xp4uXOqGioMYPHPtRo6R2nwXFTbMqkQOOqi4huaz6DLHVqnvV4PSp3WrF5lEf1YBTp2nVKLbjmi4kJzW9xNav4ZCENReI7ZKmUQtOs7ZVS+Jqu5H0aiMGxXbB0GwEp9XYaVRsJ4xuJB7jJLEFjZ9BUmtqNCm2ZlM/ktMmD7GxpmkkF03HMxRbe8ZZdM5lTEm2O5r5naVvFbxZALSiXxUfmxCVVITxU3QKhw/gHd1CSdnXLsUtbf/CEz95KnlyMNFxNtlxNlEylCwZer+EfVDCxkdGEyVjyZKxfx2KJEMxSOQKPYgjdEg1jEl6xFHtUQUw6SFx2KLzIb4OZQoZOn+HzjQOYnSwgVQXxSCXxCBC1x1V12M3HVdPo3NF3YYN36PpR2fnaQnv6OZ37X3rmTefiZunF/HbSZj/e1Sn0RlWjajmnoGEd49iuoB3DPOFxW8E3y90PCh0JAqdyULn+4WHHhQeShQeSRYeuaOdL9g1F4kX7IfPfPH+rw29X3zoQfGhRPGRZPGROc186f63Lr95OfV7Jn6WTZ6dfP/s9IOz04mzF5NnL75/9sqDs1ew/nStUH9wxLAfCvgLWS9tQB1wTrPAFEOQkuMYsF3Vhc4JVQ86bapeDFsi4M4+jAG4KOBHOmpncby4/t3uBNOaZFrfZzofMJ349djTn+jqj58aSHQNxM+cS3SdSzDuJOOOM+4FZtdbpjdN921fyflazlzOPFM8p53fXna/N77dCp/5XXu+tWvuwNyBhdLyeMWJ+MneREVvvG8wUTEYP+tOVMAlG0hUBBKlwWRpMF4aXCjdHy9v+pE6UdqWLG17v/Tkg9KT8e6+eL8r0e2KD5xNdJ+ND3kS3Z5EqTdZ6o2XehdK933b9Iemd2xv53wz537OfGn5fe1PEP6WKX34cCFnSzKnKJljXaRo4w4CC+s23jbdsd7Kvp19U/i3qAYrzEo/M2Redz+vv67Bfz/Hl5B+t6KgQ0u9Zyqo20O9V0yjvkdTt1/93t7j+UD+WlvaYVb/dSUNuLYtmlaLtW3RtW3RlTVY2xZd2xZdvaxr26Jr26LUJ7Qtyp3G5VX6tiXnQhhAOIOgLPi4IYRzCG6EYQTcz+C8CCzCCMIors2NRdIbC4s4Hxrxe5abQMDdQc6PgPuA3CRqAYQgxssIuSfZ8iDnG/UFuPNo5hBCCHjGlIsgTCNcQLiIcAljHpI3c8T38z7ldhYXxYQuI8QwtYqPTy11/4nD/+eNu4IxW56yHI/eWeI+h4k+j/B5gF9l74i7Qcvn+L8EkLZdxL0AEN08aVttn0jorRdp+fz/bYDH7NDY0ndouJcQXkbAzRnuFYQ7CK8ivIbwOsIbCH+MBXvcZkCLDIW4IbC2GfAb2Ay4RDYDLpHNAFB7hnDtR4+oRA44pooiiamOqhVbnboPSb96mNi86lpcV9ZrjmkUW5vmBJJuTR+xndKEkEQ0F4ktqmnChX+L9piWxNX2IOnTThsU20VDCy7yjxn7jYrttNGHZMIYIbYLxmZc5Lea2k2KrdM0hMRtmiC2SdMVJEczujMUW2/GiFDtjIuSLW0z4IwqPjklKqmImwGDwmbA4Kd4M+CyWuggoU9Oa84I2wBnJUzZDMA1ep14Vu206qxK2BCakDYD/MJmgH9tM+B3ezOAexe/mNZW+Km1WFvhr63wV9ZgbYW/tsJfvaxrK/y1FT71qVnhRzessm5dtuKPPuEZJMujziBZzEXLNgy4MYSn2SrgphCeZouA+z5C+kKf+wGCsnrn/hLgN73wtq628B56qoW39RNdeDfL0Iohn11beH/yC+9pYeF9CFeW0xnxI53xE32SfsoDygg9rhL5otIiR9UNasXWpHYhGRBenCjZxtSNuIhr1nRoFFuX+Py9X+MitjPi8/dLmhixXdEIS+42bYeWxNWeQuLSRg2KLWZow+V1h7HHqNj6jCNIxowcsYWNDbiibjIdMym2NtMZJGdNY8Q2brqMZMbUlaHYTmZ4hCf0GRHJtrbyXlt5r62811beayvvtZX3yhqsrbzXVt6rl3Vt5b228qY+PSvv7IuPW3Sv9pide++pV83f+11ZNVettmr+/FOtmqs+0VVzqwxC8/4IAe/ZyrQc3ttweCuC/zcYxeEXL4dv4iprEN+WgdXldXg8wFHFa6J+3zCvnvJN8boI5wciHtQXzvjjaX3xbX3CDw8046FggLuP/A8Q8IcLHP6fvvjrBc4XGOVNocjwFBfE/9OAz/UEA54Ix7GBcMVIJBzh2BCHr47j6jDGhvagN+Jn017LwWtGhidCHF4SvGo0zGuFF8Rym2nhZR2X3LzaHfDhTyOmWe4tNBrxdy/C/5HMZ4i/hhka5SJT3BEhhYteXuV28/Sw+CoP2sPTo7wRt5TEd37QY1yX4DHO0xM87ee1EfdExCr8qIHXisnSXp6GkCO8YSTi97tHA2HxvysQXlyI7wUR30hyD7U5hHcQ8BcR3HZMRh8OTrCBiYj4jg7h9wbCOYNmpQvT3364ZHhmUmiYw9x/p3E+gFHwNnwVw006Tf+E2hBP/8xTxfFfx2ee0s5q4zp7gnIkKUeccsxTplnNNdN129WcazmzOZL/gQR1MEkdjFMHV/gbZ1XXjNf3JqhNSWpTnNokW0oSVG6Syo1TuVIawQQ1laSm4tSUnIblata1rNksKUbcVJeg6pNUfZyqX1Tp6cx5Q2v8t/GZN2yLy595Q218xefhvD5/kVLRhQTmDeuvq24Y47lHE4bapBBKMt3cmzBsTxq2x+XPPJUxG54Nw8Lrx9rwrGZemzvbd20QlqMbGxvpdAfWq7qmRvoXojOLOzj6yL7ZKHiDe7NMdO+0iu6cT3TfMYrudyT/dyX/H0n+8VNuSRmekBT/tKjgGQe6TqWQelUHIZ3iyXyRuFReQlhVkJAp8cCGSC6rGtUKaVJ3EXJCPUDIGTVLyIh6ipDz6ighl9UNGoU0ir/0kFITN5pEMqDxEsJqAoQExVMfIrmkqdOSmmrbCGnX9hHSrz1HiFs7TsiENkxIRHuFkM9oW3UKOabrJqRHN0jIWd0oIWO684RwusuExHSNetKI+k5CuvSnCXHp/YRM6qcJuaC/Qshn9M0GhbQYThBy0jBAyBnDCCGjhilCzhuihFw2NBhJlxjbCekwniLktNFDiNc4Rch542VCYsYmk0KaTScJ6TadJWTIFCRkyhQl5LKpMYM0VUYXIScyBgg5Ix6ykSqXcZ4QLiNGyExGcyZpqsyThHRnDhJyNtNHyHhmmJBI5tEshdRmtRHSntVPyKksDyHerAAhwawoIZezGrNJ5bK7CDmRPUDImewRQkazOUJC2TOEXMluyVFIa043IT05ZwkZyvERMp4TJiSSc3Qdqdy644S0resjpH/dMCGedQFCgusuERJd17CeDKT1nYR0rXcRMrCeJWRk/RQh59dfJiS2vi2XtHXuICFnc8cI8eWGCYnktm5QyLENLkIGNkwQ4t8QI2RmQ8tG0ogbuwnp2ThIyNmNPkLGN0YImd5Yu0khdZtOEtK96SwhQ5vGCZnYdJmQ2KbmzWSMbu4mpGfzECHnNk8Rcn5zjJCZzS1bSBW29BDSu+UcIe4tfkImt1wk5NKW+jyFNOR1ENKZ5yJkIG+EkNE8jpBQ3gwhV/JatpLibO0hpHfrOULcW/2ETG69SMilrQ35ZCDldxLSlT9AyJn8UULG8kOEhPOvEPKZ/NYCMigKegnpKzhHiLtgghB/wTQhFwpqt5EO3tZOSMe2U4Sc3uYhxLstSMjUtighl7c1bldI0/YThJzcfoaQwe1jhPi2hwgJb79CyGe2txaSyhX2ENJbOETIucJxQiYKLxMSK2zeQQbfjm5CenacJWRoxzghEzsihEzvOMoopJY5Tkgb00dIP+MmZJjxEzLJXCDkItO4k7TOzi5CTuwcIOTMzlFCxnZyhIR2zhByZWdLERmJRd2E9BSdJWSoyEfIeFGEkOmio7tI5XYdJ6RtVz8hp3Z5CPHumiQksCtMSGTXDCFXdjXtVkjz7k5CunafIuT0bjchw7vHCPHtPk8It/syIbHdDcXk+inuIKSz+DQhruJhQjzFE4T4i0OEhItjhMwUN+4h/bOnjZD2Pb2E9O3xEOLd4ydkcs8FQi7uqS9RSENJByGdJacJcZV4CWFLgoRMlUQJuVzSUEqqXdpJSFepi5CB0hFCRkvPE8KVxgiZKW0pI2OnrJuQnrKzEsHnW2VjhPjKOEJCZTFCZsqa9iqkeW8XISf2uggZ2OslhN0bICS49yIhl/bW7VNI/b42Qtr39RHSv+8cIe5944RM7AvvU+oDOKv9sTZzVv1jbZYMumxc2OhlMGXOGn+cUwBRC0fxbj5nTD2bIRmEh8E5MxrF4BNCjEOIeVPO9eJb2uf339i/SGXQBQLM1v04o+e6at605fqeG+XxvJpEXg2i6UDSdOA6/WNT4c3um913cm/13+6Pmwrhg8bu6/S8Kf/6nqQp/1Xrq56EqShpKkKPrBSPqq9oEqbipKn4UYFbwWP9hni2I5HtuOkW3TsW0Z2jwZ2TyXnRvS/x+xJ/Bzl8rmvnDZlfzvh8xs3GhCE/aciPC5+fZOVe771lx//8cJHKxqUlwGzjjzM6UyrsTOQ5EU01SVMNlmoPFlfwhIbb6sKnnICKnjEgvIFzQJVSKwup1RNG/XU14THw2LQlnlufyK2/s1Nyz4M7h2TuBMB9WjTfR/KORN6pFd3vSPw7En8XOXyuG+QWbUldbz+yResf16L7fzMtWvVradHLn5IW7Xtcix79zbRoz6/tMv8NtuiHJjMNt68yfDhC5+hZ9azmQ4amYeKT4UONit6Im00S6Cgdzq0a3aw6BdTaWRW+2lb/oaGKNi9SMnx4VFVGw2pLhg/76Kfii300RefGqfUJakNS2oLUzmqv6q/pZ4V/wp71ezut9Rup720srj+s/t5BGvD/A2HhNw4='))))
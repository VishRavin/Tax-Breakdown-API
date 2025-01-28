ZERO_RESPONSE = {"bracket_breakdown": [{'bracket':{"min": 0, "max": 100, "rate": 0.15}, 'tax_amount': 0},
                                       ],
                 "total_tax": 0,
                 "effective_interest": 0}

FOUR_BRACKET_RESPONSE = {"bracket_breakdown": [{'bracket':{"min": 0, "max": 100, "rate": 0.15}, 'tax_amount': 15},
                                       {'bracket':{"min": 100, "max": 200, "rate": 0.17}, 'tax_amount': 17},
                                       {'bracket':{"min": 200, "max": 300, "rate": 0.20}, 'tax_amount': 20},
                                       {'bracket':{"min": 300, "max": 400, "rate": 0.32}, 'tax_amount': 16}],
                 "total_tax": 68,
                 "effective_interest": 0.19}

EXCEED_ALL_BRACKET_RESPONSE = {"bracket_breakdown": [{'bracket':{"min": 0, "max": 100, "rate": 0.15}, 'tax_amount': 15},
                                                     {'bracket':{"min": 100, "max": 200, "rate": 0.17}, 'tax_amount': 17},
                                                     {'bracket':{"min": 200, "max": 300, "rate": 0.20}, 'tax_amount': 20},
                                                     {'bracket':{"min": 300, "max": 400, "rate": 0.32}, 'tax_amount': 32},
                                                     {'bracket':{"min": 400, "rate": 0.45}, 'tax_amount': 112.5},],
                 "total_tax": 196.5,
                 "effective_interest": 0.30}

ERROR_RESPONSE_400_SALARY = {"errors":[{"code":"BAD_REQUEST","field":"","message":"400 Bad Request: Improper salary"}]}

ERROR_RESPONSE_400_YEAR = {'errors': [{'code': 'BAD_REQUEST', 'field': '', 'message': '400 Bad Request: Improper year'}]}

ONE_BRACKET_REAL_RESPONSE = {"bracket_breakdown":[{"bracket":{"max":50197,"min":0,"rate":0.15},"tax_amount":1500.0}],
                             "effective_interest":0.15,
                             "total_tax":1500.0}

TWO_BRACKET_REAL_RESPONSE = {"bracket_breakdown":[{"bracket":{"max":50197,"min":0,"rate":0.15},"tax_amount":7529.55},
                                                  {"bracket":{"max":100392,"min":50197,"rate":0.205},"tax_amount":2009.61}],
                             "effective_interest":0.16,
                             "total_tax":9539.16}

EXCEED_ALL_BRACKET_REAL_RESPONSE = {"bracket_breakdown":[{"bracket":{"max":50197,"min":0,"rate":0.15},"tax_amount":7529.55},
                                                         {"bracket":{"max":100392,"min":50197,"rate":0.205},"tax_amount":10289.97},
                                                         {"bracket":{"max":155625,"min":100392,"rate":0.26},"tax_amount":14360.58},
                                                         {"bracket":{"max":221708,"min":155625,"rate":0.29},"tax_amount":19164.07},
                                                         {"bracket":{"min":221708,"rate":0.33},"tax_amount":1086.36}],
                                    "effective_interest":0.23,
                                    "total_tax":52430.53}
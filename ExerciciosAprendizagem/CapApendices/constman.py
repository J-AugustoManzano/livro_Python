from sys import modules
class _constman:

    __M_E = 2.718281828459045
    __M_LOG2E = 1.442695040888963
    __M_LOG10E = 0.434294481903251
    __M_LN2 = 0.693147180559945
    __M_LN10 = 2.302585092994045
    __M_PI = 3.141592653589793
    __M_PI_2 = 1.570796326794896
    __M_PI_4 = 0.785398163397448
    __M_1_PI = 0.318309886183790
    __M_2_PI = 0.636619772367581
    __M_2_SQRTPI = 1.128379167095512
    __M_SQRT2 = 1.414213562373095
    __M_SQRT1_2 = 0.707106781186547

    @property
    def M_E(self):
        return self.__M_E

    @property
    def M_LOG2E(self):
        return self.__M_LOG2E

    @property
    def M_LOG10E(self):
        return self.__M_LOG10E

    @property
    def M_LN2(self):
        return self.__M_LN2

    @property
    def M_LN10(self):
        return self.__M_LN10

    @property
    def M_PI(self):
        return self.__M_PI

    @property
    def M_PI_2(self):
        return self.__M_PI_2

    @property
    def M_PI_4(self):
        return self.__M_PI_4

    @property
    def M_1_PI(self):
        return self.__M_1_PI

    @property
    def M_2_PI(self):
        return self.__M_2_PI

    @property
    def M_2_SQRTPI(self):
        return self.__M_2_SQRTPI

    @property
    def M_SQRT2(self):
        return self.__M_SQRT2

    @property
    def M_SQRT1_2(self):
        return self.__M_SQRT1_2

modules[__name__] = _constman()

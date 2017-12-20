"""
Shipping Container Classes
"""
import iso6346

class ShippingContainer:
    next_serial = 1337

    def __init__(self, owner_code, contents):
        self._owner_code = owner_code
        self._contents = contents
        self._bic = self._make_bic_code(
            owner_code=owner_code,
            serial=self._get_next_serial())

    # we can use a @classmethod instead
    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code, *args, **kwargs):
        return cls(owner_code, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, *args, **kwargs):
        return cls(owner_code, contents=list(items), *args, **kwargs)

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6))


class RefrigeratorShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0
    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              category='R')

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        if celsius > RefrigeratorShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = celsius


if __name__ == '__main__':
    c1 = ShippingContainer("MAE", "fruit")
    print(c1._bic)
    c2 = ShippingContainer.create_empty("YML")
    print(c2._bic)
    c3 = ShippingContainer.create_with_items("ABC",
            ["food", "textiles","minerals"])
    print(c3._bic)
    print(c3.__dict__)
    r1 = RefrigeratorShippingContainer(owner_code="MAE",
                                       contents=["fish", "beef", "fruit"],
                                       celsius=2)
    r2 = RefrigeratorShippingContainer.create_with_items(
        "ESC", ["broccoli, cauliflower","carrots"], celsius=2.0)
    print(r2._contents)

    r3 = RefrigeratorShippingContainer.create_empty("PPE", celsius=2.5)
    print(r3)

    print(r1._bic)

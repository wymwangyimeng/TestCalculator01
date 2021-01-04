import pytest
import yaml
from pythoncode.calculator import Calculator


def read_datas():
    with open("./resource/data.yaml", encoding='UTF-8') as f:
        datas = yaml.safe_load(f)
        # add_datas = datas["add"]
        # print(datas)
        # print(add_datas)
        return datas


class TestCalc:

    datas = read_datas()

    def setup_class(self):
        print("\n========所有用例开始前执行========")
        self.calc = Calculator()
        # self.datas = read_datas()

    def teardown_class(self):
        print("\n========所有用例结束后执行========")

    def setup_method(self):
        print("\n开始计算")

    def teardown_method(self):
        print("\n结束计算")


    @pytest.mark.parametrize("a,b,expect", datas['add'])
    def test_add(self, a, b, expect):
        res = self.calc.add(a, b)
        assert res == expect

    @pytest.mark.parametrize("a,b,expect", datas['sub'])
    def test_sub(self, a, b, expect):
        res = self.calc.sub(a, b)
        assert res == expect

    @pytest.mark.parametrize("a,b,expect", datas['mul'])
    def test_mul(self, a, b, expect):
        res = self.calc.mul(a, b)
        assert res == expect

    @pytest.mark.parametrize("a,b,expect", datas['div'])
    def test_div(self, a, b, expect):
        res = self.calc.div(a, b)
        assert res == expect

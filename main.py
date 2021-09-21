import abc
from unittest import TestCase, main

class Calculator(object):
    def calculate(self, firstValue, secondValue, operand):
        fabricOp = FabricOperation()
        operation = fabricOp.create(operand)
        if(operation == None):
            return 0
        else:
            result = operation.execute(firstValue, secondValue)
            return result

class FabricOperation(object):
    def create(self, operand):
        if(operand == 'sum'):
            return SumNumbers()
        elif (operand == 'sub'):
            return SubtractionNumbers()
        elif (operand == 'division'):
            return DivisionNumbers()
        elif (operand == 'multiply'):
            return MultiplyNumbers()

class Operation(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self, firstValue, secondValue):
        pass

class SumNumbers(Operation):
    def execute(self, firstValue, secondValue):
        result = firstValue + secondValue
        return result

class SubtractionNumbers(Operation):
    def execute(self, firstValue, secondValue):
        result = firstValue - secondValue
        return result


class DivisionNumbers(Operation):
    def execute(self, firstValue, secondValue):
        result = firstValue / secondValue
        return result


class MultiplyNumbers(Operation):
    def execute(self, firstValue, secondValue):
        result = firstValue * secondValue
        return result

class Testing(TestCase):
    def testing_multiply(self):
        calculatorM = Calculator()
        self.assertEqual(calculatorM.calculate(15, 3, 'multiply'), 45)

    def testing_sum(self):
        calculatorSum = Calculator()
        self.assertEqual(calculatorSum.calculate(200, 15, 'sum'), 215)

    def testing_sub(self):
        calculatorSub = Calculator()
        self.assertEqual(calculatorSub.calculate(1000, 500, 'sub'), 500)

    def testing_div(self):
        calculatorDiv = Calculator()
        self.assertEqual(calculatorDiv.calculate(12, 4, 'division'), 3)

        #forcing errors
    def wrong_sum(self):
        calculatorSum = Calculator()
        self.assertEqual(calculatorSum.calculate(200, 35, 'su'), 0)

    def wrong_div(self):
        calculatorDiv = Calculator()
        self.assertEqual(calculatorDiv.calculate(12, 4, 'divisio'), 0)

    def wrong_sub(self):
        calculatorSub = Calculator()
        self.assertEqual(calculatorSub.calculate(1000, 500, 'subt'), 0)

    def wrong_multiply(self):
        calculatorM = Calculator()
        self.assertEqual(calculatorM.calculate(15, 4, 'multiplyc'), 0)

calculator = Calculator()
case1 = calculator.calculate(2, 9, 'multiply')
print(case1)

case2 = calculator.calculate(2, 7, 'sum')
print(case2)

case3 = calculator.calculate(15, 3, 'subt')
print(case3)

case4 = calculator.calculate(15, 5, 'division')
print(case4)



if __name__ == '__main__':
    main()
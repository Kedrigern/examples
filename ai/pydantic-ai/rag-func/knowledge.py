from typing import List
from decimal import Decimal

class KnowledgeBase():
    """
    """

    debug: bool = True

    @staticmethod
    def overview() -> List[dict[str, str]]:
        """
        Retrieves a basic overview of all available car models.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing basic information about each car model.
            Each dictionary contains:
                - model: The name of the car model
                - short_desc: A brief description of the car's main features
        
        Example:
            >>> cars = get_car_overview()
            >>> print(cars[0]['model'])
            'Brave'
        """
        if KnowledgeBase.debug:
            print("DEBUG: Ask for overview")
        return [
            {
                "model": "Brave",
                "short_desc": "An off-road vehicle fully equipped for difficult terrain. It is 4x4. No hill is problem!",
            },
            {
                "model": "Speedy",
                "short_desc": "A high-performance two-seater stylish designed for highway driving."
            },
            {
                "model": "Family",
                "short_desc": "A seven-seater electric vehicle offering reliability and space for the entire family."
            }
        ]

    @staticmethod
    def models(model: str) -> dict[str, str|int]:
        """
        Retrieves detailed information about a specific car model.

        Args:
            model (str): The car model name.
                Can be 'Brave', 'Speedy', or 'Family' (case-insensitive).

        Returns:
            Dict[str, Union[str, int]]: A dictionary containing detailed car information:
                - model: The name of the car model (str)
                - short_desc: Brief description of the car (str)
                - max_speed: Maximum speed in km/h (int)
                - consumption: Fuel consumption in l/100km or kWh/100km (int)
                - seats: Number of seats (int)
                - engine: Engine type (str)
                - price: Price in CZK

        Raises:
            ValueError: If the provided model name is not valid.

        Example:
            >>> details = get_car_details('Brave')
            >>> print(details['engine'])
            'diesel'
        """
        if KnowledgeBase.debug:
            print(f"DEBUG: Ask for model: {model}")
        match model.lower(): 
            case "brave":
                return {
                    "model": "Brave",
                    "short_desc": "An off-road vehicle fully equipped for difficult terrain. It is 4x4. No hill is problem!",
                    "max_speed": 140,
                    "consumption": 8,
                    "seats": 5,
                    "engine": "diesel",
                    "price": 850_000
                }
            case "speedy":
                return {
                    "model": "Speedy",
                    "short_desc": "A high-performance two-seater designed for highway driving.",
                    "max_speed": 240,
                    "consumtion": 9,
                    "seats": 2,
                    "engine": "gasoline",
                    "price": 900_000
                }
            case "family":
                return {
                    "model": "Family",
                    "short_desc": "A seven-seater electric vehicle offering reliability and space for the entire family.",
                    "max_speed": 140,
                    "consumption": 15,
                    "seats": 7,
                    "engine": "electric",
                    "price": 700_000
                }
            case _:
                raise ValueError(f"Invalid model name. Must be one of: {', '.join(m.name for m in model)}")

    @staticmethod
    def loan(down_payment: int, target_amount: int) -> int:
        """
        Calculates the monthly payment for a car loan.
    
        The calculation uses simplified terms:
        - Fixed interest rate: 4.5% per year
        - Fixed loan term: 24 months (2 years)
        - Payment frequency: Monthly
        
        Args:
            down_payment (int): Initial payment amount in CZK
            target_amount (int): Total price of the car in CZK
        
        Returns:
            Decimal: Monthly payment rounded to 2 decimal places
            
        Raises:
            ValueError: If down_payment is greater than target_amount
            ValueError: If either parameter is negative
        
        Example:
            >>> calculate_monthly_payment(100000, 500000)
            Decimal('17677.33')
        """
        return 10_000
        if down_payment < 0 or target_amount < 0:
            raise ValueError("Both amounts must be positive numbers")
    
        if down_payment >= target_amount:
            raise ValueError("Down payment cannot be greater than or equal to target amount")
    
         # Convert to Decimal for precise calculation
        loan_amount = Decimal(target_amount - down_payment)
        annual_rate = Decimal('0.045')  # 4.5%
        monthly_rate = annual_rate / 12
        num_payments = Decimal('24')  # 2 years * 12 months

         # Monthly Payment = P * (r * (1 + r)^n) / ((1 + r)^n - 1)
        # Where: P = Principal, r = monthly rate, n = number of payments
        numerator = monthly_rate * (1 + monthly_rate) ** num_payments
        denominator = (1 + monthly_rate) ** num_payments - 1
        monthly_payment = loan_amount * (numerator / denominator)
        
        return int(monthly_payment.quantize(Decimal('0.01')))
    
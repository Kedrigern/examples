{- Example of using guards in Haskell
Script is absolutly free/libre, but with no guarantee.
Author: Ondrej Profant -}

isNeg :: Int -> Bool
isNeg x = if x < 0 
		then True 
		else False

myabs :: Int -> Int
myabs x
	| x < 0 = -x
	| x >= 0 = x
	
myabs2 :: Int -> Int
myabs2 x = if isNeg(x)
	then -x
	else x
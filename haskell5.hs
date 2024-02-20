import System.Environment (getArgs)


subtract1:: [Int] -> [Int]

subtract1 []= []
subtract1 (x:xs) =(x - 1) : subtract1 xs


main :: IO ()
main = do
    args <- getArgs
    let numbers = map read args :: [Int]
        result = subtract1 numbers
        resultStrings = map show result
        outputString = unwords resultStrings
    putStrLn outputString

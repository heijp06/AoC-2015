module Main where

import Lib
import Utils
import System.Clipboard (setClipboardString)
import Data.List.Split (splitOn)
import Data.List ((!!),sort)

main :: IO ()
main = do
    xs <- rows <$> readFile "data.txt" -- Data item per row.
    -- xs <- groups <$> readFile "data.txt" -- Groups of data items separated by empty rows.
    -- xs <- multi <$> readFile "data.txt" -- Multi line strings separated by empty rows.
    putStr "Part one: "
    let x = sum $ map f xs
    print x
    clip x

    putStr "Part two: "
    let y = sum $ map g xs
    print y
    clip y

f :: String -> Integer
f xs = let (a:b:c:_) = sort . map read $ splitOn "x" xs in a*b+2*(a*b+b*c+c*a)

g :: String -> Integer
g xs = let (a:b:c:_) = sort . map read $ splitOn "x" xs in 2*(a+b)+a*b*c

clip :: Show a => a -> IO ()
clip = setClipboardString . show
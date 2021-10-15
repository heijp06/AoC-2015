module Main where

import Lib
import Utils
import System.Clipboard (setClipboardString)

main :: IO ()
main = do
    xs <- readFile "data.txt" -- Data item per row.
    -- xs <- groups <$> readFile "data.txt" -- Groups of data items separated by empty rows.
    -- xs <- multi <$> readFile "data.txt" -- Multi line strings separated by empty rows.
    putStr "Part one: "
    let x = foldr (\c acc -> if c == '(' then acc+1 else acc-1) 0 xs
    print x
    clip x

    putStr "Part two: "
    let ys = takeWhile (>=0) $ scanl (\acc c -> if c == '(' then acc+1 else acc-1) 0 xs
    let y = length ys
    print y
    clip y


clip :: Show a => a -> IO ()
clip = setClipboardString . show
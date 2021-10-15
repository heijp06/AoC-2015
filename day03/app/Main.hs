module Main where

import Lib
import Utils
import System.Clipboard (setClipboardString)
import qualified Data.Set as S
import Data.List.Split (chunksOf)

main :: IO ()
main = do
    xs <- readFile "data.txt" -- Data item per row.

    putStr "Part one: "
    let x = S.size . snd $ foldl f ((0,0), S.singleton (0,0)) xs
    print x
    clip x

    putStr "Part two: "
    let y = S.size . snd . foldl g (((0,0), (0,0)), S.singleton (0,0)) $ chunksOf 2 xs
    print y
    clip y

f :: ((Int,Int), S.Set (Int,Int)) -> Char -> ((Int,Int), S.Set (Int,Int))
f (pos,set) c = let newPos = move pos c in (newPos,S.insert newPos set)

g :: (((Int,Int), (Int,Int)), S.Set (Int,Int)) -> String -> (((Int,Int), (Int,Int)), S.Set (Int,Int))
g ((santa,robot),set) (s:r:_) = ((newSanta,newRobot), S.insert newSanta $ S.insert newRobot set)
    where
        newSanta = move santa s
        newRobot = move robot r

move :: (Int,Int) -> Char -> (Int,Int)
move (x,y) c = case c of
    'v' -> (x,y-1)
    '^' -> (x,y+1)
    '<' -> (x-1,y)
    '>' -> (x+1,y)

clip :: Show a => a -> IO ()
clip = setClipboardString . show
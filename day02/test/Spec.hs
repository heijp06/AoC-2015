import Control.Monad     (unless)
import Test.Hspec        (Spec, describe, expectationFailure, it, shouldBe)
import Test.Hspec.Runner (configFastFail, defaultConfig, hspecWith)

import Lib

main :: IO ()
main = hspecWith defaultConfig {configFastFail = True} specs

specs :: Spec
specs =
    describe "foo" $
        it "foo" $ 1 `shouldBe` 1
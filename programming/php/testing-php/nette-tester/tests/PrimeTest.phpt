<?php namespace Test;

use Tester\Assert;

require __DIR__ . '/bootstrap.php';

$prime = new \Ntest\Model\Prime();

\Tester\Assert::false($prime->isPrime(0));
\Tester\Assert::false($prime->isPrime(-1));
\Tester\Assert::false($prime->isPrime(-542));

\Tester\Assert::true($prime->isPrime(2));


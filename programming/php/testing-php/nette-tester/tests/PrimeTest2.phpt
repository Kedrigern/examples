<?php namespace Test;

use Tester\Assert;

$container = require __DIR__ . '/bootstrap.php';

class Prime2Test extends \Tester\TestCase
{
  private $container;

  function __construct($container)
  {
    $this->container = $container;
  }

  function setUp()
  {}


  function testZero()
  {
    $prime = new \Ntest\Model\Prime();

    Assert::false($prime->isPrime(0));
  }

  function testNegative()
  {
    $prime = new \Ntest\Model\Prime();

    Assert::false($prime->isPrime(-1));
    Assert::false($prime->isPrime(-42));
  }

  function testFail()
  {
    Assert::true(false);
  }
}

id(new Prime2Test($container))->run();


<?php namespace Ntest\Model;

class Prime extends \Nette\Object
{
    /**
     * Is given number prime number?
     *
     * @param int $n
     * @return bool
     */
    public function isPrime($n)
    {
        if( !is_int($n) ) {
            throw new Exception();
        }
        if( $n < 2 ) return false;

        $target = intval( round( sqrt($n), 0 ) );
        for($i = 2; $i < $target; $i++ )
        {
            if( $n % $i === 0 ) {
                return false;
            }
        }
        return true;
    }
}

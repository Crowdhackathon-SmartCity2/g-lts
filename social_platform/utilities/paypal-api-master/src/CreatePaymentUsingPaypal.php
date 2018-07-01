<?php

// # Create Payment using PayPal as payment method
// This sample code demonstrates how you can process a
// PayPal Account based Payment.
// API used: /v1/payments/payment

require  __DIR__ .'/PayPal-PHP-SDK/autoload.php';
require  __DIR__ .'/common.php';
require  __DIR__ .'/index.html';


$apiContext = new \PayPal\Rest\ApiContext(
    new PayPal\Auth\OAuthTokenCredential(
        'AcyKeVTWkvPdp2lYgNaoCkFmEJYQImlnyTBFYz3B-RYVRjo39mqPYiI90AZtHo3FzB1fVLL9HUdN5IkB',
        'EIQAlcYL6xNEs_-vUdSkYJ54YMHaItVB2Mz31Da3OdXJio1ei6hBxo2_eUoG8rtYnmifFn9uL4-CywDg'

    )
);



$apiContext->setConfig(
    array(
        'log.LogEnabled' => true,
        'log.FileName' => 'PayPal.log',
        'log.LogLevel' => 'DEBUG'
    )
);

$product = $_POST["product"];
$price = $_POST["price"];
$tax=2;
$total = $price+$tax;

use PayPal\Api\Amount;
use PayPal\Api\Details;
use PayPal\Api\Item;
use PayPal\Api\ItemList;
use PayPal\Api\Payer;
use PayPal\Api\Payment;
use PayPal\Api\RedirectUrls;
use PayPal\Api\Transaction;




// ### Payer
// A resource representing a Payer that funds a payment
// For paypal account payments, set payment method
// to 'paypal'.
$payer = new Payer();
$payer->setPaymentMethod("paypal");

// ### Itemized information
// (Optional) Lets you specify item wise
// information
$item1 = new Item();
$item1->setName($product)
    ->setCurrency('USD')
    ->setQuantity(1)
    ->setSku("123123") // Similar to `item_number` in Classic API
    ->setPrice($price);


$itemList = new ItemList();
$itemList->setItems(array($item1));

// ### Additional payment details
// Use this optional field to set additional
// payment information such as tax, shipping
// charges etc.
$details = new Details();
$details->setTax($tax)
        ->setSubtotal($price);

// ### Amount
// Lets you specify a payment amount.
// You can also specify additional details
// such as shipping, tax.
$amount = new Amount();
$amount->setCurrency("USD")
    ->setTotal($total)
    ->setDetails($details);

// ### Transaction
// A transaction defines the contract of a
// payment - what is the payment for and who
// is fulfilling it.
$transaction = new Transaction();
$transaction->setAmount($amount)
    ->setItemList($itemList)
    ->setDescription("Payment description")
    ->setInvoiceNumber(uniqid());

// ### Redirect urls
// Set the urls that the buyer must be redirected to after
// payment approval/ cancellation.
$redirectUrls = new \PayPal\Api\RedirectUrls();
$redirectUrls ->setReturnUrl("http://localhost/ExecPayment.php?success=true");
$redirectUrls ->setCancelUrl("http://localhost/ExecPayment.php?success=false");

// ### Payment
// A Payment Resource; create one using
// the above types and intent set to 'sale'
$payment = new Payment();
$payment->setIntent("sale")
    ->setPayer($payer)
    ->setRedirectUrls($redirectUrls)
    ->setTransactions(array($transaction));


// For Sample Purposes Only.
$request = clone $payment;

// ### Create Payment
// Create a payment by calling the 'create' method
// passing it a valid apiContext.
// (See bootstrap.php for more on `ApiContext`)
// The return object contains the state and the
// url to which the buyer must be redirected to
// for payment approval
try {
    $payment->create($apiContext);
} catch (Exception $ex) {
    // NOTE: PLEASE DO NOT USE RESULTPRINTER CLASS IN YOUR ORIGINAL CODE. FOR SAMPLE ONLY
    ResultPrinter::printError("Created Payment Using PayPal. Please visit the URL to Approve.", "Payment", null, $request, $ex);
    exit(1);
}

// ### Get redirect url
// The API response provides the url that you must redirect
// the buyer to. Retrieve the url from the $payment->getApprovalLink()
// method
$approvalUrl = $payment->getApprovalLink();

// NOTE: PLEASE DO NOT USE RESULTPRINTER CLASS IN YOUR ORIGINAL CODE. FOR SAMPLE ONLY
ResultPrinter::printResult("Created Payment Using PayPal. Please visit the URL to Approve.", "Payment", "<a href='$approvalUrl' >$approvalUrl</a>", $request, $payment);

return $payment;

/* This will give an error. Note the output
 * above, which is before the header() call */
//header('$approvalUrl');


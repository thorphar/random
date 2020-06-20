<?php
// Your ID and token
$blogID = '8070105920543249955';
$authToken = 'OAuth 2.0 token here';

// The data to send to the API
$postData = array(
    'to' => $_POST['to'],    
    'from' => $_POST['from'],
    'project' => $_POST['project']
);

// Setup cURL
$ch = curl_init('https://prod-27.uksouth.logic.azure.com:443/workflows/03c2ec8f72d74469b4ea83975d52ddc6/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=_FdfXEkUqb9pGiKWZyDX6ANVgdMgE4845STDTwgtivo');
curl_setopt_array($ch, array(
    CURLOPT_POST => TRUE,
    CURLOPT_RETURNTRANSFER => TRUE,
    CURLOPT_HTTPHEADER => array(
        //'Authorization: '.$authToken,
        'Content-Type: application/json'
    ),
    CURLOPT_POSTFIELDS => json_encode($postData)
));

// Send the request
$response = curl_exec($ch);

// Check for errors
if($response === FALSE){
    die(curl_error($ch));
}

// Decode the response
$responseData = json_decode($response, TRUE);

// Print the date from the response
echo $responseData['published'];
?>
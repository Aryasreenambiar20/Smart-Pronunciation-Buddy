function startSpeaking() {

    const word = document.getElementById("word").value.trim();

    if(word===""){

        alert("Please enter a word.");

        return;

    }

    const resultBox=document.getElementById("result");

    resultBox.className="";

    resultBox.innerHTML="🎧 Listening... Please speak clearly.";

    fetch("/check",{

        method:"POST",

        body:new URLSearchParams({

            target:word

        })

    })

    .then(response=>response.json())

    .then(data=>{

        resultBox.className="";

        if(data.result==="correct"){

            resultBox.classList.add("correct");

        }

        else if(data.result==="almost correct"){

            resultBox.classList.add("almost");

        }

        else if(data.result==="incorrect"){

            resultBox.classList.add("incorrect");

        }

        else{

            resultBox.classList.add("failed");

        }

        if(data.result==="failed"){

            resultBox.innerHTML=`
            ❌ <b>${data.message}</b>
            `;

            return;

        }

        resultBox.innerHTML=`

        <b>🎯 Target Word:</b> ${word}<br><br>

        <b>🗣️ You Said:</b> ${data.spoken}<br><br>

        <b>📊 Similarity:</b> ${data.similarity}%<br><br>

        <b>✅ Result:</b> ${data.result.toUpperCase()}

        `;

        if(data.result==="correct"){

            document.getElementById("word").value="";

        }

    })

    .catch(error=>{

        resultBox.className="failed";

        resultBox.innerHTML="❌ Something went wrong.";

        console.log(error);

    });

}
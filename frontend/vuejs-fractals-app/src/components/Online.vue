<template>
    <div class="fractalContainer">
            <div class="imgContainer">
                <img v-bind:src="fractalImg" alt="">
            </div>
            <div class="formContainer">
                <h1>Data to generate fractal</h1>
                <form v-on:submit.prevent="sendFractal()">
                    <div class="inputBox">
                        <label for="">Name:</label>
                        <select v-model="fractal.name">
                            <option v-for="fractalName in fractalsName":value="fractalName">{{ fractalName }}</option>
                        </select>
                    </div>
                    <div class="inputBox">
                        <label for="">Max iterations:</label>
                        <input type="text" v-model="fractal.maxIt">
                    </div>
                    <div class="inputBox">
                        <label for="">re:</label>
                        <input type="text" v-model="fractal.re">
                    </div>
                    <div class="inputBox">
                        <label for="">im:</label>
                        <input type="text" v-model="fractal.im">
                    </div>
                    <div class="inputBox">
                        <label for="">h:</label>
                        <input type="text" v-model="fractal.h">
                    </div>
                    <div class="inputBox">
                        <label for="">w:</label>
                        <input type="text" v-model="fractal.w">
                    </div>
                    <div class="inputBox">
                        <label for="">p1:</label>
                        <input type="text" v-model="fractal.p1">
                    </div>
                    <div class="inputBox">
                        <label for="">k1:</label>
                        <input type="text" v-model="fractal.k1">
                    </div>
                    <div class="inputBox">
                        <label for="">p2:</label>
                        <input type="text" v-model="fractal.p2">
                    </div>
                    <div class="inputBox">
                        <label for="">k2:</label>
                        <input type="text" v-model="fractal.k2">
                    </div>
                    <div class="buttonContainer">
                        <button type="submit">Send</button>
                    </div>
                </form>
            </div>
        </div>
</template>

<script>
export default {
    
    data(){
        return{
            username: 'tomek',
            data: '',
            fractalImg: '',
            fractalsName: [
                "mandelbrot",
                "julia"
            ],
            fractal: {
                name: 'julia',
                maxIt: 200,
                re: -0.10,
                im: 0.65,
                h: 500,
                w: 500,
                p1: -1.5,
                k1: 1.5,
                p2: -1.5,
                k2: 1.5
            }
        }
    },
    methods: {
        sendFractal: function(){
        const BASE_URL = 'http://35.238.239.157:8000/fractal/';
        const requesOption = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(this.fractal)
        };
            this.$http.post(BASE_URL, requesOption
            ).then(function(data){
                this.getFractal();
            });
        },

        getFractal: function(){
            const RE_URL = 'http://35.238.239.157:8000/preview64/?';
            var self = this;
            setInterval(function() {
                self.$http.get('http://35.238.239.157:8000/preview64/?user='+self.username).then(function(response) {
                   if(response.status == "200") {
                        let fBase64 = response.bodyText;
                        self.fractalImg = 'data:image/png;base64,'+fBase64;
                    }
                })
            }, 3000);
        }
    },
   
}
</script>
<style scoped>
.fractalContainer{
    position: relative;
    width: 98%;
    height: 80vh;
    display: flex;
    background: rgba(255,255,255,0.6);
    margin: 0 1%;
}
.fractalContainer .imgContainer{
    width: 75%;
    border: 3px solid #09002b;
    margin: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.fractalContainer .formContainer {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.fractalContainer .formContainer h1{
    padding: 20px 0;
}
.fractalContainer .formContainer form{
    height: 40%;
    display: grid;
    grid-template-columns: auto auto;
    align-items: center;
    margin: 30px 0;
}

.fractalContainer .formContainer form .inputBox{
    display: flex;
    flex-direction: column;
    margin: 10px;
    color: #09002b;
}
.fractalContainer .formContainer form .inputBox input, select {
    border: #FFF;
}
</style>

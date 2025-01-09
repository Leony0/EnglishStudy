import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import React from "react";
import axios from "axios";

import Word from "./components/Word"

//ここはかなりシンプルなコードしか書かないようにする
//127.0.0.1:8000/word/all/


const App = () => {
 return( 
   <>
   
    <h1>英単語アプリ</h1>
    <Word />
   
   </>
 )
};

export default App;

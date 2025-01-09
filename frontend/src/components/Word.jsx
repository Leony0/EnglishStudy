import List from "./List"
import Form from "./Form"

import { useEffect, useState } from 'react'
import axios from "axios";

const Word = () => {
    const [words, setWords] = useState([]);
    const [newWord, setNewWord] = useState({
        word: "",
        meaning: "",
        example_sentence: "",
      });
    

    useEffect(() => {
      const getWord = async () => {
        const res =await axios.get("http://localhost:8000/word/all/")
        console.log(res)
        setWords(res.data)
      }
      getWord();
    },[])

    
    const deleteWord = async (id) => {
      await axios.delete(`http://localhost:8000/word/${id}`)
      setWords((prevWords) => prevWords.filter((word) => word.id !== id));
    
    };

    const createWord = async () => {
        const response = await axios.post("http://localhost:8000/word/", newWord);
        setWords((prevWords) => [...prevWords, response.data]); 
        setNewWord({ word: "", meaning: "", example_sentence: "" }); 
    };

    const handleSubmit = (e) => {
        e.preventDefault(); 
        createWord();
    };


  
    return (
      <>
        <Form newWord={newWord} setNewWord={setNewWord} handleSubmit={handleSubmit}/>
        <List words={words} deleteWord={deleteWord}/>
      </>
    )
}

export default Word;
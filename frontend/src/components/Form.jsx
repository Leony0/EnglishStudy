import { useEffect, useState } from 'react'

const Form = ({newWord, setNewWord, handleSubmit}) => {

    return (
        <div>
            <h2>単語を追加</h2>
            <form onSubmit={handleSubmit}>
                <input
                type="text"
                placeholder="単語"
                value={newWord.word}
                onChange={(e) => setNewWord({ ...newWord, word: e.target.value })}
                />
                <input
                type="text"
                placeholder="意味"
                value={newWord.meaning}
                onChange={(e) => setNewWord({ ...newWord, meaning: e.target.value })}
                />
                <input
                type="text"
                placeholder="例文"
                value={newWord.example_sentence}
                onChange={(e) => setNewWord({ ...newWord, example_sentence: e.target.value })}
                />
                <button type="submit">登録</button>
            </form>
        </div>
    )
}

export default Form;
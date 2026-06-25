import React, { useState, useMemo } from 'react';
import Deck from './components/Deck';
import defaultFlashcards from './data/flashcards.json';
import customQuestionsRaw from '../../questions_template.md?raw';
import { parseMarkdownCards } from './utils/mdParser';
import './App.css';

function App() {
  const [selectedChapter, setSelectedChapter] = useState('All');
  const [excludeMemorized, setExcludeMemorized] = useState(false);

  // Merge default flashcards and custom flashcards from markdown template
  const flashcardsData = useMemo(() => {
    try {
      const customCards = parseMarkdownCards(customQuestionsRaw);
      return [...defaultFlashcards, ...customCards];
    } catch (error) {
      console.error('Failed to parse custom questions template:', error);
      return defaultFlashcards;
    }
  }, [customQuestionsRaw]);

  // Extract unique chapters for the selector
  const chapters = useMemo(() => {
    const uniqueChapters = new Set(flashcardsData.map(card => card.chapter));
    return ['All', ...Array.from(uniqueChapters)];
  }, [flashcardsData]);

  // Filter cards based on selected chapter
  const currentDeck = useMemo(() => {
    if (selectedChapter === 'All') return flashcardsData;
    return flashcardsData.filter(card => card.chapter === selectedChapter);
  }, [selectedChapter, flashcardsData]);

  return (
    <div className="app-container">
      <header>
        <h1>전기기사 플래시</h1>
        <p>Premium Flashcards for Electromagnetics</p>
      </header>

      <div className="controls-bar glass">
        <div className="deck-selector">
          <label htmlFor="chapter-select" style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>
            Chapter:
          </label>
          <select 
            id="chapter-select"
            value={selectedChapter} 
            onChange={(e) => setSelectedChapter(e.target.value)}
          >
            {chapters.map(chapter => (
              <option key={chapter} value={chapter}>{chapter}</option>
            ))}
          </select>
        </div>

        <label className="toggle-label">
          <input 
            type="checkbox" 
            checked={excludeMemorized} 
            onChange={(e) => setExcludeMemorized(e.target.checked)} 
          />
          <div className="toggle-switch"></div>
          Exclude Memorized
        </label>
      </div>

      <main>
        <Deck 
          cards={currentDeck} 
          excludeMemorized={excludeMemorized} 
        />
      </main>

      <footer>
        <p>Built with React & Vite. Formulas curated from 전기자기학 치트키.</p>
      </footer>
    </div>
  );
}

export default App;

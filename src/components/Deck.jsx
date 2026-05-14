import React, { useState, useEffect } from 'react';
import { ArrowLeft, ArrowRight, Shuffle, CheckCircle, RotateCcw } from 'lucide-react';
import Flashcard from './Flashcard';
import './Deck.css';

const Deck = ({ cards, excludeMemorized }) => {
  const [currentCards, setCurrentCards] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [memorizedIds, setMemorizedIds] = useState(() => {
    try {
      const saved = localStorage.getItem('memorizedIds');
      if (saved) return new Set(JSON.parse(saved));
    } catch (e) {
      console.error('Failed to load memorized cards', e);
    }
    return new Set();
  });

  useEffect(() => {
    try {
      localStorage.setItem('memorizedIds', JSON.stringify(Array.from(memorizedIds)));
    } catch (e) {
      console.error('Failed to save memorized cards', e);
    }
  }, [memorizedIds]);

  const prevCardsRef = React.useRef(cards);
  const prevExcludeRef = React.useRef(excludeMemorized);

  // Initialize and filter cards based on props
  useEffect(() => {
    let filtered = cards;
    if (excludeMemorized) {
      filtered = cards.filter(card => !memorizedIds.has(card.id));
    }
    setCurrentCards(filtered);
    
    // If cards or excludeMemorized changed, reset index to 0
    if (prevCardsRef.current !== cards || prevExcludeRef.current !== excludeMemorized) {
      setCurrentIndex(0);
      prevCardsRef.current = cards;
      prevExcludeRef.current = excludeMemorized;
    } else {
      // If only memorizedIds changed, keep the index (bound by new length)
      setCurrentIndex(prev => {
        if (filtered.length === 0) return 0;
        return Math.min(prev, filtered.length - 1);
      });
    }
  }, [cards, excludeMemorized, memorizedIds]);

  const handleNext = () => {
    if (currentIndex < currentCards.length - 1) {
      setCurrentIndex(currentIndex + 1);
    }
  };

  const handlePrev = () => {
    if (currentIndex > 0) {
      setCurrentIndex(currentIndex - 1);
    }
  };

  const handleShuffle = () => {
    const shuffled = [...currentCards].sort(() => Math.random() - 0.5);
    setCurrentCards(shuffled);
    setCurrentIndex(0);
  };

  const toggleMemorized = () => {
    if (currentCards.length === 0) return;
    
    const currentCard = currentCards[currentIndex];
    setMemorizedIds(prev => {
      const newSet = new Set(prev);
      if (newSet.has(currentCard.id)) {
        newSet.delete(currentCard.id);
      } else {
        newSet.add(currentCard.id);
      }
      return newSet;
    });
  };

  const resetMemorized = () => {
    setMemorizedIds(new Set());
  };

  if (currentCards.length === 0) {
    return (
      <div className="empty-state">
        <h3>All caught up! 🎉</h3>
        <p>You have memorized all cards in this selection.</p>
        <button onClick={resetMemorized} className="btn">
          <RotateCcw size={18} />
          Reset Memorized Status
        </button>
      </div>
    );
  }

  const currentCard = currentCards[currentIndex];
  const isCurrentMemorized = memorizedIds.has(currentCard.id);
  const progress = ((currentIndex + 1) / currentCards.length) * 100;

  return (
    <div className="deck-container">
      <div className="progress-container">
        <div className="progress-text">
          {currentIndex + 1} / {currentCards.length}
        </div>
        <div className="progress-bar">
          <div className="progress-fill" style={{ width: `${progress}%` }}></div>
        </div>
      </div>

      <Flashcard 
        card={currentCard} 
        isFlipped={isFlipped} 
        setIsFlipped={setIsFlipped}
        isMemorized={isCurrentMemorized}
      />

      <div className="deck-controls">
        <button 
          className="btn-icon" 
          onClick={handlePrev} 
          disabled={currentIndex === 0}
          aria-label="Previous card"
        >
          <ArrowLeft size={24} />
        </button>

        <div style={{ display: 'flex', gap: '1rem' }}>
          <button 
            className={`btn btn-outline ${isCurrentMemorized ? 'memorized-btn' : ''}`}
            onClick={toggleMemorized}
            style={{ borderColor: isCurrentMemorized ? 'var(--success-color)' : '', color: isCurrentMemorized ? 'var(--success-color)' : '' }}
          >
            <CheckCircle size={20} />
            {isCurrentMemorized ? 'Memorized' : 'Mark as Memorized'}
          </button>
          <button className="btn btn-outline" onClick={handleShuffle}>
            <Shuffle size={20} />
            Shuffle
          </button>
        </div>

        <button 
          className="btn-icon" 
          onClick={handleNext} 
          disabled={currentIndex === currentCards.length - 1}
          aria-label="Next card"
        >
          <ArrowRight size={24} />
        </button>
      </div>
    </div>
  );
};

export default Deck;

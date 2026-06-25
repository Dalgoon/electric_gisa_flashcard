/**
 * Parses markdown text into an array of flashcard objects.
 * 
 * Target format:
 * ## Chapter
 * ### Topic
 * - **Q**: Question
 * - **A**: Answer
 * 
 * @param {string} mdText - Raw markdown content
 * @returns {Array} Array of parsed flashcard objects
 */
export function parseMarkdownCards(mdText) {
  if (!mdText) return [];
  
  const lines = mdText.split(/\r?\n/);
  const cards = [];
  
  let currentChapter = '미분류';
  let currentTopic = '기타';
  
  let mode = 'none'; // 'none', 'question', 'answer'
  let activeCard = null;
  
  // Simple helper to generate a stable, deterministic hash code for card IDs
  function hashCode(str) {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      const chr = str.charCodeAt(i);
      hash = ((hash << 5) - hash) + chr;
      hash |= 0; // Convert to 32bit integer
    }
    return Math.abs(hash).toString(36);
  }

  function commitActiveCard() {
    if (activeCard && activeCard.question.trim() && activeCard.answer.trim()) {
      const idStr = `${activeCard.chapter}-${activeCard.topic}-${activeCard.question.trim()}`;
      activeCard.id = `custom-${hashCode(idStr)}`;
      activeCard.question = activeCard.question.trim();
      activeCard.answer = activeCard.answer.trim();
      cards.push(activeCard);
    }
    activeCard = null;
  }

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmed = line.trim();
    
    // Skip divider lines
    if (trimmed === '---' || trimmed === '===') {
      continue;
    }
    
    // 1. Detect Chapter (## Chapter Name)
    if (trimmed.startsWith('## ')) {
      commitActiveCard();
      currentChapter = trimmed.substring(3).trim();
      currentTopic = ''; // Clear topic when chapter changes
      mode = 'none';
      continue;
    }
    
    // 2. Detect Topic (### Topic Name)
    if (trimmed.startsWith('### ')) {
      commitActiveCard();
      currentTopic = trimmed.substring(4).trim();
      mode = 'none';
      continue;
    }
    
    // 3. Detect Question
    // Matches: - **Q**: Text or **Q**: Text or - Q: Text or Q: Text or - **질문**: Text or **질문**: Text
    const qMatch = trimmed.match(/^(?:-\s*)?\*\*(?:Q|질문)\*\*\s*:\s*(.*)/i) || 
                   trimmed.match(/^(?:-\s*)?(?:Q|질문)\s*:\s*(.*)/i);
    if (qMatch) {
      commitActiveCard();
      activeCard = {
        chapter: currentChapter,
        topic: currentTopic || '기타',
        question: qMatch[1],
        answer: '',
        isCustom: true
      };
      mode = 'question';
      continue;
    }
    
    // 4. Detect Answer
    // Matches: - **A**: Text or **A**: Text or - A: Text or A: Text or - **답변**: Text or **답변**: Text
    const aMatch = trimmed.match(/^(?:-\s*)?\*\*(?:A|답변|답)\*\*\s*:\s*(.*)/i) || 
                   trimmed.match(/^(?:-\s*)?(?:A|답변|답)\s*:\s*(.*)/i);
    if (aMatch && activeCard) {
      activeCard.answer = aMatch[1];
      mode = 'answer';
      continue;
    }
    
    // 5. Accumulate content for multi-line question or answer
    if (mode === 'question' && activeCard) {
      activeCard.question += '\n' + line;
    } else if (mode === 'answer' && activeCard) {
      activeCard.answer += '\n' + line;
    }
  }
  
  // Commit the last active card if any
  commitActiveCard();
  
  return cards;
}

declare module 'research-agent-ui' {
  import React from 'react';

  export interface ResearchAgentProps {
    apiUrl?: string;
    apiKey?: string;
    defaultPrompt?: string;
    onResultsChange?: (results: any) => void;
    theme?: any;
  }

  export const ResearchAgent: React.FC<ResearchAgentProps>;
}
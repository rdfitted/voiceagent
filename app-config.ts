import type { AppConfig } from './lib/types';

export const APP_CONFIG_DEFAULTS: AppConfig = {
  companyName: 'Fitted Automation',
  pageTitle: 'Voice AI Assistant',
  pageDescription: 'A powerful voice AI assistant with internet search and website analysis',

  supportsChatInput: true,
  supportsVideoInput: true,
  supportsScreenShare: true,
  isPreConnectBufferEnabled: true,

  logo: '/fitted-logo.png',
  accent: '#0074FF',
  logoDark: '/fitted-logo.png',
  accentDark: '#0074FF',
  startButtonText: 'Start conversation',
};
